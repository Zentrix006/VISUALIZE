"""Xfce legacy tray bridge. GTK3 runs separately from the GTK4 UI."""
import signal
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def emit(command):
    print(command, flush=True)


def main():
    icon = Gtk.StatusIcon.new_from_icon_name("network-transmit-receive")
    icon.set_tooltip_text("VISUALIZE — network connections")
    icon.set_visible(True)
    icon.connect("activate", lambda *_: emit("open"))
    menu = Gtk.Menu()
    for title, command in (("Connections", "open"), ("Open network map", "expand"), ("Quit VISUALIZE", "quit")):
        item = Gtk.MenuItem(label=title)
        item.connect("activate", lambda _, value=command: emit(value))
        menu.append(item)
    menu.show_all()
    icon.connect("popup-menu", lambda _, button, timestamp: menu.popup(None, None, None, None, button, timestamp))
    signal.signal(signal.SIGTERM, lambda *_: Gtk.main_quit())
    Gtk.main()


if __name__ == "__main__":
    main()
