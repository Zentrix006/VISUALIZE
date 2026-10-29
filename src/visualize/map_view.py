"""Custom GTK4 drawing area for the interactive connection map."""

import math

from gi.repository import GLib, Gtk


BG = (0.035, 0.055, 0.075)
GRID = (0.11, 0.16, 0.20)
CYAN = (0.28, 0.78, 0.98)
CYAN_SOFT = (0.16, 0.48, 0.64)
MUTED = (0.49, 0.58, 0.65)
WHITE = (0.88, 0.93, 0.96)
GREEN = (0.31, 0.83, 0.66)
ORANGE = (0.98, 0.66, 0.31)


class MapView(Gtk.DrawingArea):
    def __init__(self, connections, on_select):
        super().__init__()
        self.connections = connections
        self.on_select = on_select
        self.selected_id = connections[0]["id"] if connections else None
        self.phase = 0.0
        self.set_content_width(680)
        self.set_content_height(560)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_draw_func(self.draw)

        click = Gtk.GestureClick.new()
        click.connect("released", self.handle_click)
        self.add_controller(click)

        motion = Gtk.EventControllerMotion.new()
        motion.connect("motion", self.handle_motion)
        self.add_controller(motion)

        GLib.timeout_add(70, self.animate)

    def animate(self):
        self.phase = (self.phase + 0.012) % 1.0
        self.queue_draw()
        return GLib.SOURCE_CONTINUE

    def point_for(self, connection, width, height):
        x, y = connection["position"]
        return width * (0.08 + x * 0.84), height * (0.08 + y * 0.84)

    @staticmethod
    def text(cr, value, x, y, size=11, color=WHITE, bold=False):
        cr.select_font_face(
            "Inter" if bold else "Sans",
            0,
            1 if bold else 0,
        )
        cr.set_font_size(size)
        cr.set_source_rgba(*color, 0.96)
        cr.move_to(x, y)
        cr.show_text(value)

    @staticmethod
    def bezier_point(p0, p1, p2, p3, t):
        u = 1 - t
        return (
            u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1],
        )

    def draw(self, _area, cr, width, height):
        cr.set_source_rgb(*BG)
        cr.paint()
        self.draw_grid(cr, width, height)

        center = (width * 0.5, height * 0.51)
        for index, connection in enumerate(self.connections):
            if connection["state"] != "Active":
                continue
            endpoint = self.point_for(connection, width, height)
            self.draw_link(cr, center, endpoint, connection, index)

        for connection in self.connections:
            if connection["state"] == "Active":
                self.draw_node(cr, self.point_for(connection, width, height), connection)
        self.draw_system(cr, center)

        self.text(cr, "OUTBOUND CONNECTIONS", 24, 30, 10, MUTED, True)
        self.text(cr, "DEMO DATA · SIMULATED", width - 174, 30, 10, GREEN, True)

    def draw_grid(self, cr, width, height):
        cr.set_line_width(1)
        cr.set_source_rgba(*GRID, 0.36)
        for x in range(0, int(width), 52):
            cr.move_to(x, 0)
            cr.line_to(x, height)
        for y in range(0, int(height), 52):
            cr.move_to(0, y)
            cr.line_to(width, y)
        cr.stroke()

        # Soft concentric guides make the local-system focus clear without
        # suggesting that the map is a geographic projection.
        cx, cy = width * 0.5, height * 0.51
        cr.set_source_rgba(*CYAN_SOFT, 0.18)
        cr.set_line_width(1)
        for radius in (90, 175, 260):
            cr.arc(cx, cy, radius, 0, math.tau)
            cr.stroke()

    def draw_link(self, cr, start, end, connection, index):
        dx, dy = end[0] - start[0], end[1] - start[1]
        distance = math.hypot(dx, dy) or 1
        bend = (index % 2 * 2 - 1) * min(48, distance * 0.12)
        normal = (-dy / distance, dx / distance)
        p1 = (start[0] + dx * 0.33 + normal[0] * bend, start[1] + dy * 0.33 + normal[1] * bend)
        p2 = (start[0] + dx * 0.72 + normal[0] * bend, start[1] + dy * 0.72 + normal[1] * bend)
        selected = connection["id"] == self.selected_id
        color = CYAN if selected else CYAN_SOFT

        cr.new_path()
        cr.move_to(*start)
        cr.curve_to(*p1, *p2, *end)
        cr.set_line_width(8 if selected else 4)
        cr.set_source_rgba(*color, 0.10 if selected else 0.07)
        cr.stroke()

        cr.new_path()
        cr.move_to(*start)
        cr.curve_to(*p1, *p2, *end)
        cr.set_line_width(2.1 if selected else 1.25)
        cr.set_source_rgba(*color, 0.96 if selected else 0.68)
        cr.stroke()

        t = (self.phase + index * 0.17) % 1.0
        particle = self.bezier_point(start, p1, p2, end, t)
        cr.arc(*particle, 2.5 if selected else 1.8, 0, math.tau)
        cr.set_source_rgba(*WHITE, 0.94)
        cr.fill()

    def draw_node(self, cr, point, connection):
        x, y = point
        selected = connection["id"] == self.selected_id
        radius = 10 if selected else 7

        cr.arc(x, y, radius + 8, 0, math.tau)
        cr.set_source_rgba(*CYAN, 0.10 if selected else 0.045)
        cr.fill()
        cr.arc(x, y, radius, 0, math.tau)
        cr.set_source_rgba(0.035, 0.09, 0.13, 0.98)
        cr.fill_preserve()
        cr.set_line_width(2 if selected else 1.4)
        cr.set_source_rgba(*CYAN, 0.98 if selected else 0.75)
        cr.stroke()

        label = connection["domain"]
        self.text(cr, label, x + 14, y - 9, 10, WHITE if selected else MUTED, selected)
        self.text(cr, connection["traffic"], x + 14, y + 7, 9, CYAN, False)

    def draw_system(self, cr, point):
        x, y = point
        cr.arc(x, y, 42, 0, math.tau)
        cr.set_source_rgba(*CYAN, 0.09)
        cr.fill()

        cr.save()
        cr.translate(x, y)
        cr.rotate(math.pi / 4)
        cr.rectangle(-22, -22, 44, 44)
        cr.set_source_rgba(0.055, 0.12, 0.17, 1)
        cr.fill_preserve()
        cr.set_line_width(2)
        cr.set_source_rgba(*CYAN, 0.95)
        cr.stroke()
        cr.restore()

        cr.set_source_rgba(*CYAN, 0.92)
        cr.arc(x, y, 6, 0, math.tau)
        cr.fill()
        self.text(cr, "THIS SYSTEM", x - 37, y + 58, 10, WHITE, True)
        self.text(cr, "Linux host", x - 26, y + 74, 9, MUTED)

    def handle_click(self, _gesture, _press_count, x, y):
        width, height = self.get_width(), self.get_height()
        for connection in reversed(self.connections):
            if connection["state"] != "Active":
                continue
            nx, ny = self.point_for(connection, width, height)
            if math.hypot(nx - x, ny - y) <= 24:
                self.selected_id = connection["id"]
                self.on_select(connection)
                self.queue_draw()
                return

    def handle_motion(self, _controller, x, y):
        width, height = self.get_width(), self.get_height()
        hit = any(
            connection["state"] == "Active"
            and math.hypot(*(
                self.point_for(connection, width, height)[i] - (x, y)[i]
                for i in range(2)
            )) <= 24
            for connection in self.connections
        )
        self.set_cursor_from_name("pointer" if hit else "default")
