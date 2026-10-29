"""Compact tray panel; shares the full window's preview state."""
from gi.repository import Gtk


class CompactWindow(Gtk.ApplicationWindow):
    def __init__(self, app, full_window):
        super().__init__(application=app, title="VISUALIZE · Connections")
        self.full_window = full_window
        self.set_default_size(430, 480)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        for edge in ("top", "bottom", "start", "end"):
            getattr(box, "set_margin_" + edge)(18)
        box.append(Gtk.Label(label="CONNECTIONS · DEMO DATA", xalign=0))
        self.rows = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_child(self.rows)
        box.append(scroll)
        expand = Gtk.Button(label="Open network map")
        expand.connect("clicked", self.expand)
        box.append(expand)
        self.set_child(box)
        self.set_hide_on_close(True)

    def refresh(self):
        while self.rows.get_first_child():
            self.rows.remove(self.rows.get_first_child())
        for connection in self.full_window.connections:
            if connection["state"] != "Active":
                continue
            row = Gtk.Button(label=f'{connection["service"]}  ·  {connection["traffic"]}')
            row.connect("clicked", self.select, connection)
            self.rows.append(row)

    def select(self, _button, connection):
        self.full_window.select_connection(connection)
        self.expand(None)

    def expand(self, _button):
        self.set_visible(False)
        self.full_window.present()
