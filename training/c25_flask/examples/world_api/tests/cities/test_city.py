import unittest

from cities import City


class TestCity(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_city_id(self):
        # Creation
        city = City(10)
        self.assertEqual(city.city_id, 10)

        # Modification
        city.city_id = 20
        self.assertEqual(city.city_id, 20)

        # None Value
        with self.assertRaises(ValueError):
            city.city_id = 0

        # Invalid Value
        with self.assertRaises(ValueError):
            city.city_id = -10
        with self.assertRaises(ValueError):
            city.city_id = '10'

    def test_name(self):
        # Creation
        city = City(1, 'Santiago')
        self.assertEqual(city.name, 'Santiago')

        # Modification
        city.name = 'SANTIAGO'
        self.assertEqual(city.name, 'SANTIAGO')

        # None Value
        with self.assertRaises(ValueError):
            city.name = ''

        # Invalid Value
        with self.assertRaises(ValueError):
            city.name = 'SG'
        with self.assertRaises(ValueError):
            city.name = 1

    def test_country_code(self):
        # Creation
        city = City(1, 'Santiago', 'CHI')
        self.assertEqual(city.country_code, 'CHI')

        # Modification
        city.country_code = 'CHL'
        self.assertEqual(city.country_code, 'CHL')

        # None Value
        with self.assertRaises(ValueError):
            city.country_code = ''

        # Invalid Value
        with self.assertRaises(ValueError):
            city.country_code = 'CH'
        with self.assertRaises(ValueError):
            city.country_code = 'CHILE'
        with self.assertRaises(ValueError):
            city.country_code = 1

    def test_district(self):
        # Creation
        city = City(1, 'Santiago', 'CHI', 'Santiago')
        self.assertEqual(city.district, 'Santiago')

        # Modification
        city.district = 'Santiago Centro'
        self.assertEqual(city.district, 'Santiago Centro')

        # None Value
        with self.assertRaises(ValueError):
            city.district = ''

        # Invalid Value
        with self.assertRaises(ValueError):
            city.district = 'SC'
        with self.assertRaises(ValueError):
            city.district = 1

    def test_population(self):
        # Creation
        city = City(1, 'Santiago', 'CHI', 'Santiago', 1_000_000)
        self.assertEqual(city.population, 1_000_000)

        # Modification
        city.population = 10_000_000
        self.assertEqual(city.population, 10_000_000)

        # None Value
        city.population = 0
        self.assertEqual(city.population, 0)

        # Invalid Value
        with self.assertRaises(ValueError):
            city.population = -10
        with self.assertRaises(ValueError):
            city.population = '10'


module_name = 'tests.TestCity'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    unittest.main()
else:
    print('Importing {} class'.format(module_name))
