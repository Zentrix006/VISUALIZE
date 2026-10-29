import ipaddress
import unittest

from visualize.data import CONNECTIONS


DOCUMENTATION_NETWORKS = tuple(
    ipaddress.ip_network(network)
    for network in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")
)


class SampleDataTests(unittest.TestCase):
    def test_connection_ids_are_unique(self):
        ids = [connection["id"] for connection in CONNECTIONS]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_endpoint_uses_documentation_domain_and_address(self):
        for connection in CONNECTIONS:
            with self.subTest(service=connection["service"]):
                self.assertTrue(
                    connection["domain"].endswith((".example.com", ".example.net", ".example.org"))
                )
                address = ipaddress.ip_address(connection["address"].split(":", 1)[0])
                self.assertTrue(any(address in network for network in DOCUMENTATION_NETWORKS))

    def test_sample_connections_have_service_location_and_protocol(self):
        for connection in CONNECTIONS:
            with self.subTest(service=connection["service"]):
                self.assertTrue(connection["service"])
                self.assertTrue(connection["location"])
                self.assertTrue(connection["protocol"])
                self.assertEqual(connection["state"], "Active")


if __name__ == "__main__":
    unittest.main()
