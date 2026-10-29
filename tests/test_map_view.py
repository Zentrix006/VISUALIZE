import unittest

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from visualize.data import CONNECTIONS
from visualize.map_view import MapView


class MapViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Gtk.init()

    def test_all_sample_nodes_fit_inside_map(self):
        view = MapView(CONNECTIONS, lambda _connection: None)
        width, height = 1000, 700

        for connection in CONNECTIONS:
            with self.subTest(service=connection["service"]):
                x, y = view.point_for(connection, width, height)
                self.assertGreater(x, 0)
                self.assertLess(x, width)
                self.assertGreater(y, 0)
                self.assertLess(y, height)

    def test_link_animation_interpolation_keeps_endpoints(self):
        start = (100.0, 200.0)
        control_a = (200.0, 100.0)
        control_b = (300.0, 300.0)
        end = (400.0, 200.0)

        self.assertEqual(
            MapView.bezier_point(start, control_a, control_b, end, 0),
            start,
        )
        self.assertEqual(
            MapView.bezier_point(start, control_a, control_b, end, 1),
            end,
        )


if __name__ == "__main__":
    unittest.main()
