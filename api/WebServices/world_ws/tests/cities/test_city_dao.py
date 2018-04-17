import unittest

from cities import City
from cities import CityDAO


class TestCityDAO(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        dao = CityDAO()

        # Success Creation
        # Original Creation
        city = City(1, 'Santiago', 'CHL', 'Santiago', 10_000_000)
        save_city1 = dao.create(city)
        self.assertEqual(save_city1.name, city.name)
        # Repeat Creation
        save_city2 = dao.create(city)
        self.assertEqual(save_city2.name, city.name)
        self.assertNotEqual(save_city1.city_id, save_city2.city_id)

        # Deleting Created Info
        required_city = City(1, 'Santiago', 'CHL', 'Santiago', 10_000_000)
        retrived_cities = dao.retrive_by_data(required_city)
        for retrived_city in retrived_cities:
            dao.delete(retrived_city)

        # Failed Creation
        # Bad Input
        with self.assertRaises(ValueError):
            dao.create(1)

    def test_update(self):
        dao = CityDAO()

        # Success Update
        city = City(1, 'Santiago', 'CHL', 'Santiago', 10_000_000)
        save_city = dao.create(city)
        save_city.population += 1_000_000
        updated_city = dao.update(save_city)
        self.assertEqual(updated_city.population, 11_000_000)

        # Deleting Created Info
        dao.delete(updated_city)

        # Failed Update
        # No info
        # Bad Input
        with self.assertRaises(ValueError):
            dao.update(1)

    def test_delete(self):
        dao = CityDAO()

        # Creating Info
        city = City(1, 'Santiago', 'CHL', 'Santiago', 10_000_000)
        save_city = dao.create(city)

        # Success Delete
        deleted_city = dao.delete(save_city)
        retrived_city = dao.retrive(deleted_city)
        self.assertEqual(retrived_city, None)

        # Failed Delete
        # No info
        # Bad Input
        with self.assertRaises(ValueError):
            dao.update(1)

    def test_retrive(self):
        dao = CityDAO()

        # Success Retriving
        city = dao.retrive(City(1))
        self.assertEqual(city.name, 'Kabul')

        # Failed Retriving
        # No info
        city = dao.retrive(City(10000))
        self.assertEqual(city, None)
        # Bad Input
        with self.assertRaises(ValueError):
            dao.retrive(1)

    def test_retrive_previous(self):
        dao = CityDAO()

        # Success Retriving
        city = dao.retrive_previous(City(2))
        self.assertEqual(city.name, 'Kabul')
        # Last
        city = dao.retrive_previous(City(5000))
        self.assertEqual(city.name, 'Rafah')

        # Failed Retriving
        # No info
        city = dao.retrive_previous(City(1))
        self.assertEqual(city, None)
        # Bad Input
        with self.assertRaises(ValueError):
            dao.retrive_previous(1)

    def test_retrive_next(self):
        dao = CityDAO()

        # Success Retriving
        city = dao.retrive_next(City(1))
        self.assertEqual(city.name, 'Qandahar')

        # Failed Retriving
        # No info
        city = dao.retrive_next(City(50000))
        self.assertEqual(city, None)
        # Bad Input
        with self.assertRaises(ValueError):
            dao.retrive_next(1)

    def test_retrive_by_data(self):
        dao = CityDAO()

        # Success Retriving
        # All Equal
        city = City(1, 'Kabul', 'AFG', 'Kabol', 1780000)
        retrived_city = dao.retrive_by_data(city)[-1]
        self.assertEqual(city, retrived_city)
        # Wrong ID but the rest Equal
        city = City(10000, 'Kabul', 'AFG', 'Kabol', 1780000)
        retrived_city = dao.retrive_by_data(city)[-1]
        self.assertEqual(city.name, retrived_city.name)

        # Failed Retriving
        # No info (Wrong Data)
        city = City(1, 'Kabul', 'AFG', 'Kabol', 178)
        retrived_city = dao.retrive_by_data(city)
        self.assertEqual(retrived_city, [])
        # Bad Input
        with self.assertRaises(ValueError):
            dao.retrive_by_data([1, 'Kabul', 'AFG', 'Kabol', 1780000])

    def test_retrive_all(self):
        dao = CityDAO()

        # Success Retriving
        # Default offset and limit
        cities = dao.retrive_all()
        self.assertEqual(len(cities), 20)
        # Default offset and Custom limit
        cities = dao.retrive_all(limit=50)
        self.assertEqual(len(cities), 50)
        self.assertEqual(cities[0].name, 'Kabul')
        # Default limit and Custom offset
        cities = dao.retrive_all(offset=10)
        self.assertEqual(len(cities), 20)
        self.assertEqual(cities[0].name, 'Groningen')

        # Failed Retriving
        # Null limit
        cities = dao.retrive_all(limit=0)
        self.assertEqual(cities, [])
        # Bad limit
        with self.assertRaises(ValueError):
            cities = dao.retrive_all(limit='50')
        with self.assertRaises(ValueError):
            cities = dao.retrive_all(limit=-50)
        # Bad offset
        with self.assertRaises(ValueError):
            cities = dao.retrive_all(offset='50')
        with self.assertRaises(ValueError):
            cities = dao.retrive_all(offset=-50)


module_name = 'tests.TestCityDAO'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    unittest.main()
else:
    print('Importing {} class'.format(module_name))
