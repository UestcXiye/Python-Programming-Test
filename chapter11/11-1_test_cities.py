import unittest
from city_function import city_country


class CityCountryCase(unittest.TestCase):
    """
    测试city_function.py
    """
    def test_city_country(self):
        format_combo = city_country('santiago', 'chile')
        self.assertEqual(format_combo, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
