import unittest
from main import sort, STANDARD, SPECIAL, REJECT


class TestSortMethod(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(sort(10, 10, 10, 5), STANDARD)

    def test_special_bulky(self):
        self.assertEqual(sort(200, 10, 10, 5), SPECIAL)

    def test_special_heavy(self):
        self.assertEqual(sort(10, 10, 10, 25), SPECIAL)

    def test_reject_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 25), REJECT)

    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), SPECIAL)

    def test_edge_case_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), SPECIAL)

    def test_edge_case_mass(self):
        self.assertEqual(sort(10, 10, 10, 20), SPECIAL)

    def test_invalid_negative_values(self):
        with self.assertRaises(ValueError):
            sort(-10, 10, 10, 5)

    def test_invalid_zero_values(self):
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 5)

    def test_invalid_non_numeric_values(self):
        with self.assertRaises(TypeError):
            sort("10", 10, 10, 5)


if __name__ == "__main__":
    unittest.main()