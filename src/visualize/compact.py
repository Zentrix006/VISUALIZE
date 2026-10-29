"""Compact tray panel; shares the full window's preview state."""
from gi.repository import Gtk


def label(text, style):
    widget = Gtk.Label(label=text, xalign=0)
    widget.add_css_class(style)
    return widget


class CompactWindow(Gtk.ApplicationWindow):
    def __init__(self, app, full_window):
        super().__init__(application=app, title="VISUALIZE · Connections")
        self.full_window = full_window
        self.set_default_size(460, 640)
        header = Gtk.HeaderBar()
        header.set_title_widget(label("VISUALIZE", "brand-name"))
        self.set_titlebar(header)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        for edge in ("top", "bottom", "start", "end"):
            getattr(box, "set_margin_" + edge)(20)
        box.append(label("Network activity", "compact-title"))
        self.summary = label("", "compact-subtitle")
        box.append(self.summary)
        box.append(label("DEMO DATA · speeds are simulated", "compact-subtitle"))
        self.rows = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_child(self.rows)
        box.append(scroll)
        expand = Gtk.Button(label="Open network map  →")
        expand.add_css_class("expand-button")
        expand.connect("clicked", self.expand)
        box.append(expand)
        self.set_child(box)
        self.set_hide_on_close(True)
        self.connect("map", lambda *_: self.refresh())

    def refresh(self):
        while self.rows.get_first_child():
            self.rows.remove(self.rows.get_first_child())
        connections = [item for item in self.full_window.connections if item["state"] == "Active"]
        self.summary.set_text(f"{len(connections)} active connections · This system")
        if not connections:
            self.rows.append(label("No active connections in this preview.", "compact-subtitle"))
        for connection in connections:
            row = Gtk.Button()
            row.add_css_class("compact-row")
            content = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
            text = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4, hexpand=True)
            text.append(label(connection["service"], "connection-name"))
            text.append(label(connection.get("direction", "Outgoing") + " · " + connection["app"], "connection-domain"))
            content.append(text)
            content.append(label(connection["traffic"], "rate"))
            row.set_child(content)
            row.connect("clicked", self.select, connection)
            self.rows.append(row)

    def select(self, _button, connection):
        self.full_window.select_connection(connection)
        self.expand(None)

    def expand(self, _button):
        self.set_visible(False)
        self.full_window.present()
