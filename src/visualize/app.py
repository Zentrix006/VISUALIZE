"""GTK4 desktop prototype for VISUALIZE."""

from pathlib import Path
import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Gdk, Gtk

from .data import CONNECTIONS
from .map_view import MapView


CSS = Path(__file__).with_name("style.css")


def make_label(text, css_class=None, xalign=0):
    label = Gtk.Label(label=text, xalign=xalign)
    label.set_wrap(True)
    if css_class:
        label.add_css_class(css_class)
    return label


class VisualizeWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="VISUALIZE")
        self.set_default_size(1440, 900)
        self.set_size_request(1050, 680)
        self.connections = [dict(item) for item in CONNECTIONS]
        self.selected = self.connections[0]

        self.install_css()
        self.set_titlebar(self.build_header())
        self.set_child(self.build_layout())
        self.refresh_details()
        self.refresh_connection_list()

    def install_css(self):
        provider = Gtk.CssProvider()
        provider.load_from_path(str(CSS))
        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(
            display,
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

    def build_header(self):
        header = Gtk.HeaderBar()
        header.add_css_class("topbar")

        brand = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        mark = make_label("V", "brand-mark")
        brand.append(mark)
        wordmark = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        wordmark.append(make_label("VISUALIZE", "brand-name", 0))
        wordmark.append(make_label("NETWORK MAP", "brand-caption", 0))
        brand.append(wordmark)
        header.set_title_widget(brand)

        status = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        status.append(make_label("●", "status-dot"))
        status.append(make_label("PREVIEW MODE", "status-text"))
        status.append(make_label("·", "status-separator"))
        status.append(make_label("DEMO DATA", "demo-chip"))
        header.pack_end(status)
        return header

    def build_layout(self):
        shell = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        shell.add_css_class("app-shell")

        shell.append(self.build_rail())
        shell.append(self.build_sidebar())
        shell.append(self.build_map_column())
        shell.append(self.build_inspector())
        return shell

    def build_rail(self):
        rail = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        rail.add_css_class("nav-rail")
        for symbol, tip, active in (
            ("⌘", "System map", True),
            ("◷", "Connection history", False),
            ("⚙", "Settings", False),
        ):
            button = Gtk.Button(label=symbol)
            button.set_tooltip_text(tip)
            button.add_css_class("rail-button")
            if active:
                button.add_css_class("rail-button-active")
            rail.append(button)
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        rail.append(spacer)
        rail.append(make_label("0.1", "rail-version"))
        return rail

    def build_sidebar(self):
        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.set_size_request(236, -1)
        sidebar.add_css_class("sidebar")

        heading = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        heading.add_css_class("section-heading")
        heading.append(make_label("CONNECTIONS", "section-title", 0))
        self.connection_count = make_label("06", "count-chip")
        heading.append(self.connection_count)
        sidebar.append(heading)
        sidebar.append(make_label("OUTBOUND · LIVE VIEW", "section-subtitle", 0))

        self.connection_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.connection_list.set_margin_top(14)
        sidebar.append(self.connection_list)

        note = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=7)
        note.add_css_class("sidebar-note")
        note.set_valign(Gtk.Align.END)
        note.set_vexpand(True)
        note.append(make_label("ABOUT THIS PREVIEW", "note-title", 0))
        note.append(make_label(
            "Connections and locations are synthetic. This preview does not inspect or change your network.",
            "note-copy",
            0,
        ))
        sidebar.append(note)
        return sidebar

    def build_map_column(self):
        column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        column.add_css_class("map-column")

        toolbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        toolbar.add_css_class("map-toolbar")
        title_group = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        title_group.append(make_label("SYSTEM MAP", "map-title", 0))
        title_group.append(make_label("Your system at the center of its outbound activity", "map-subtitle", 0))
        toolbar.append(title_group)
        spacer = Gtk.Box()
        spacer.set_hexpand(True)
        toolbar.append(spacer)
        toolbar.append(make_label("●", "legend-dot"))
        toolbar.append(make_label("ACTIVE LINK", "legend-label"))
        column.append(toolbar)

        map_frame = Gtk.Frame()
        map_frame.add_css_class("map-frame")
        self.map_view = MapView(self.connections, self.select_connection)
        map_frame.set_child(self.map_view)
        map_frame.set_hexpand(True)
        map_frame.set_vexpand(True)
        column.append(map_frame)

        footer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=14)
        footer.add_css_class("map-footer")
        footer.append(make_label("↗  OUTBOUND TRAFFIC", "footer-label"))
        footer.append(make_label("·", "footer-separator"))
        footer.append(make_label("SELECT A SERVICE TO INSPECT", "footer-label"))
        column.append(footer)
        return column

    def build_inspector(self):
        panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        panel.set_size_request(310, -1)
        panel.add_css_class("inspector")

        header = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        header.add_css_class("inspector-heading")
        header.append(make_label("SERVICE DETAILS", "section-title", 0))
        header.append(make_label("Selected remote endpoint", "section-subtitle", 0))
        panel.append(header)

        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        card.add_css_class("service-card")
        self.service_name = make_label("", "service-name", 0)
        self.service_domain = make_label("", "service-domain", 0)
        self.service_state = make_label("", "service-state", 0)
        card.append(self.service_name)
        card.append(self.service_domain)
        card.append(self.service_state)
        panel.append(card)

        location = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        location.add_css_class("detail-section")
        location.append(make_label("LOCATION", "detail-section-title", 0))
        self.location_value = make_label("", "location-value", 0)
        self.provider_value = make_label("", "detail-muted", 0)
        location.append(self.location_value)
        location.append(self.provider_value)
        panel.append(location)

        details = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        details.add_css_class("detail-section")
        details.append(make_label("CONNECTION", "detail-section-title", 0))
        self.detail_rows = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        details.append(self.detail_rows)
        panel.append(details)

        traffic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=9)
        traffic.add_css_class("detail-section")
        traffic.append(make_label("TRAFFIC", "detail-section-title", 0))
        self.traffic_value = make_label("", "traffic-value", 0)
        traffic.append(self.traffic_value)
        self.traffic_bar = Gtk.ProgressBar()
        self.traffic_bar.set_fraction(0.62)
        self.traffic_bar.add_css_class("traffic-progress")
        traffic.append(self.traffic_bar)
        self.sent_value = make_label("", "detail-muted", 0)
        self.received_value = make_label("", "detail-muted", 0)
        traffic.append(self.sent_value)
        traffic.append(self.received_value)
        panel.append(traffic)

        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        panel.append(spacer)

        self.action_button = Gtk.Button(label="Simulate disconnect")
        self.action_button.add_css_class("simulate-button")
        self.action_button.connect("clicked", self.simulate_disconnect)
        panel.append(self.action_button)
        panel.append(make_label("Demo action only · no firewall rules are changed", "action-note", 0.5))
        return panel

    def refresh_connection_list(self):
        child = self.connection_list.get_first_child()
        while child:
            next_child = child.get_next_sibling()
            self.connection_list.remove(child)
            child = next_child

        active_count = sum(item["state"] == "Active" for item in self.connections)
        self.connection_count.set_text(f"{active_count:02}")
        for item in self.connections:
            row = Gtk.Button()
            row.add_css_class("connection-row")
            if item["id"] == self.selected["id"]:
                row.add_css_class("connection-row-selected")
            row.connect("clicked", lambda _button, conn=item: self.select_connection(conn))

            content = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            dot = make_label("●" if item["state"] == "Active" else "○", "connection-dot")
            if item["state"] != "Active":
                dot.add_css_class("connection-dot-muted")
            text = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
            text.set_hexpand(True)
            text.append(make_label(item["service"], "connection-name", 0))
            text.append(make_label(item["domain"], "connection-domain", 0))
            content.append(dot)
            content.append(text)
            row.set_child(content)
            self.connection_list.append(row)

    def select_connection(self, connection):
        self.selected = connection
        self.map_view.selected_id = connection["id"]
        self.map_view.queue_draw()
        self.refresh_details()
        self.refresh_connection_list()

    def add_detail_row(self, key, value):
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        row.add_css_class("detail-row")
        row.append(make_label(key, "detail-key", 0))
        value_label = make_label(value, "detail-value", 1)
        value_label.set_hexpand(True)
        row.append(value_label)
        self.detail_rows.append(row)

    def refresh_details(self):
        item = self.selected
        self.service_name.set_text(item["service"])
        self.service_domain.set_text(item["domain"])
        self.service_state.set_text("●  " + item["state"].upper())
        self.service_state.remove_css_class("state-ended")
        if item["state"] != "Active":
            self.service_state.add_css_class("state-ended")
        self.location_value.set_text(item["location"] + "  ·  approximate")
        self.provider_value.set_text(item["provider"])
        self.traffic_value.set_text(item["traffic"] + " current rate")
        self.sent_value.set_text("↑  " + item["sent"] + " sent")
        self.received_value.set_text("↓  " + item["received"] + " received")

        child = self.detail_rows.get_first_child()
        while child:
            next_child = child.get_next_sibling()
            self.detail_rows.remove(child)
            child = next_child
        self.add_detail_row("Application", item["app"])
        self.add_detail_row("Remote address", item["address"])
        self.add_detail_row("Protocol", item["protocol"])
        self.add_detail_row("Latency", item["latency"])

        if item["state"] == "Active":
            self.action_button.set_label("Simulate disconnect")
            self.action_button.set_sensitive(True)
        else:
            self.action_button.set_label("Reconnect in demo")
            self.action_button.set_sensitive(True)

    def simulate_disconnect(self, _button):
        if self.selected["state"] == "Active":
            self.selected["state"] = "Ended (demo)"
        else:
            self.selected["state"] = "Active"
        self.refresh_details()
        self.refresh_connection_list()
        self.map_view.queue_draw()


class VisualizeApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="dev.visualize.NetworkMap")

    def do_activate(self):
        window = self.props.active_window
        if not window:
            window = VisualizeWindow(self)
        window.present()


def main():
    app = VisualizeApp()
    app.run(sys.argv)
