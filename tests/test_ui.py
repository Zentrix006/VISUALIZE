import unittest

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from visualize.app import VisualizeWindow


class PreviewInteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Gtk.init()

    def test_service_selection_and_demo_disconnect(self):
        window = VisualizeWindow(None)
        try:
            connection = window.connections[1]
            window.select_connection(connection)

            self.assertEqual(window.service_domain.get_text(), connection["domain"])
            self.assertEqual(window.location_value.get_text().split("  ·")[0], connection["location"])

            sibling = dict(connection, id="another-session")
            window.connections.append(sibling)
            window.simulate_disconnect(None)
            self.assertEqual(sibling["state"], "Ended (demo)")
            self.assertEqual(connection["state"], "Ended (demo)")
            self.assertEqual(window.service_state.get_text(), "●  ENDED (DEMO)")

            window.simulate_disconnect(None)
            self.assertEqual(connection["state"], "Active")
        finally:
            window.close()


if __name__ == "__main__":
    unittest.main()
