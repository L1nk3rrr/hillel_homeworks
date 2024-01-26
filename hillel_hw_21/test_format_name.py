import unittest

from format_name import formatted_name


class TestFormattedName(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(formatted_name("valentyn", "starushok", "l1nk3r"), "Valentyn L1nk3r Starushok")

    def test_without_middle_name(self):
        self.assertEqual(formatted_name("valentyn", "starushok"), "Valentyn Starushok")

    def test_empty_strings(self):
        self.assertEqual(formatted_name("", "", ""), "")

    def test_only_first_name(self):
        self.assertEqual(formatted_name("valentyn", ""), "Valentyn")

    def test_only_last_name(self):
        self.assertEqual(formatted_name("", "starushok"), "Starushok")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            formatted_name(123, "starushok")
        with self.assertRaises(TypeError):
            formatted_name("valentyn", 3.14)
        with self.assertRaises(TypeError):
            formatted_name("valentyn", "starushok", [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
