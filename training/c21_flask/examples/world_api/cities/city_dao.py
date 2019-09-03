# -*- coding:utf-8 -*-

from tools import DAO

from cities.city import City


class CityDAO(DAO):

    def create(self, city):
        # print('--> Creating via CityDAO')
        if isinstance(city, City):
            try:
                sql = '''INSERT INTO city (name, countrycode, district, population)
                         VALUES (%s, %s, %s, %s)'''
                self.dbman.write(sql, city.name, city.country_code,
                                 city.district, city.population)
                return self.retrive_by_data(city)[-1]
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.CREATE')

    def retrive(self, city):
        # print('--> Retriving via CityDAO')
        if isinstance(city, City):
            try:
                sql = '''SELECT * FROM city WHERE id=%s LIMIT 1'''
                result = self.dbman.read(sql, city.city_id)
                return self.tocity(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.RETRIVE')

    def retrive_by_data(self, city):
        # print('--> Retriving by Data via CityDAO')
        if isinstance(city, City):
            try:
                sql = '''SELECT * FROM city
                         WHERE name=%s AND countrycode=%s AND district=%s AND population=%s'''
                results = self.dbman.readmany(sql, city.name, city.country_code,
                                              city.district, city.population)
                cities = [self.tocity(result) for result in results]
                return cities
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.RETRIVE_BY_DATA')

    def retrive_all(self, offset=0, limit=20):
        # print('--> Retriving All via CityDAO')
        if isinstance(offset, int) and isinstance(limit, int):
            if offset >= 0 and limit >= 0:
                try:
                    sql = '''SELECT * FROM city LIMIT %s, %s'''
                    results = self.dbman.readmany(sql, offset, limit)
                    cities = [self.tocity(result) for result in results]
                    return cities
                except Exception as e:
                    raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only possitive integer values supported by CITYDAO.RETRIVE_ALL')

    def retrive_next(self, city):
        # print('--> Retriving Next via CityDAO')
        if isinstance(city, City):
            try:
                sql = '''SELECT * FROM city WHERE id>%s ORDER BY id LIMIT 1'''
                result = self.dbman.read(sql, city.city_id)
                return self.tocity(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.RETRIVE_NEXT')

    def retrive_previous(self, city):
        # print('--> Retriving Previous via CityDAO')
        if isinstance(city, City):
            try:
                sql = '''SELECT * FROM city WHERE id<%s ORDER BY id DESC LIMIT 1'''
                result = self.dbman.read(sql, city.city_id)
                return self.tocity(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.RETRIVE_PREVIOUS')

    def update(self, city):
        # print('--> Updating via CityDAO')
        if isinstance(city, City):
            try:
                if(self.retrive(city)):
                    sql = '''UPDATE city
                             SET name=%s, countrycode=%s, district=%s, population=%s
                             WHERE id=%s'''
                    self.dbman.write(sql, city.name, city.country_code, city.district, city.population,
                                     city.city_id)
                    return self.retrive(city)
                else:
                    return None
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.UPDATE')

    def delete(self, city):
        # print('--> Deleting via CityDAO')
        if isinstance(city, City):
            try:
                saved_city = self.retrive(city)
                if(saved_city):
                    sql = '''DELETE FROM city WHERE id=%s'''
                    self.dbman.write(sql, city.city_id)
                    return saved_city
                else:
                    return None
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only City Instance values supported by CITYDAO.DELETE')

    @staticmethod
    def tocity(result):
        if result:
            city_id, name, country_code, district, population = result
            city = City(city_id, name, country_code, district, population)
            # print('    {}'.format(city))
            return city
        return None


module_name = 'cities.CityDAO'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
