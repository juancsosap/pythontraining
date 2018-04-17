# -*- coding:utf-8 -*-

from tools.dao import DAO

from countries.country import Country


class CountryDAO(DAO):

    def create(self, country):
        # print('--> Creating via CountryDAO')
        if isinstance(country, Country):
            try:
                sql = '''INSERT INTO country (code, name, continent, region,
                                              surface_area, independent_year,
                                              population, life_expectation, gnp,
                                              gnp_old, local_name, government_form,
                                              head_of_state, capital, code2)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                self.dbman.write(sql, country.country_code, country.name, country.continent, country.region,
                                 country.surface_area, country.independent_year, country.population,
                                 country.life_expectation, country.gnp, country.gnp_old,
                                 country.local_name, country.government_form, country.head_of_state,
                                 country.capital, country.code2)
                return self.retrive_by_data(country)[-1]
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only Country Instance values supported by COUNTRYDAO.CREATE')

    def retrive(self, country):
        # print('--> Retriving via CountryDAO')
        if isinstance(country, Country):
            try:
                sql = '''SELECT * FROM country WHERE code=%s LIMIT 1'''
                result = self.dbman.read(sql, country.country_code)
                return self.tocountry(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only Country Instance values supported by COUNTRYDAO.RETRIVE')

    def retrive_by_data(self, country):
        # print('--> Retriving by Data via CountryDAO')
        if isinstance(country, Country):
            try:
                sql = '''SELECT * FROM country
                         WHERE name=%s AND continent=%s AND region=%s AND
                               surface_area=%s AND independent_year=%s AND
                               population=%s AND life_expectation=%s AND gnp=%s AND
                               gnp_old=%s AND local_name=%s AND government_form=%s AND
                               head_of_state=%s AND capital=%s AND code2=%s'''
                results = self.dbman.readmany(sql, country.name, country.continent, country.region,
                                              country.surface_area, country.independent_year,
                                              country.population, country.life_expectation,
                                              country.gnp, country.gnp_old, country.local_name,
                                              country.government_form, country.head_of_state,
                                              country.capital, country.code2)
                countries = [self.tocountry(result) for result in results]
                return countries
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only Country Instance values supported by COUNTRYDAO.RETRIVE_BY_DATA')

    def retrive_all(self, offset=0, limit=20):
        # print('--> Retriving All via CountryDAO')
        if isinstance(offset, int) and isinstance(limit, int):
            if offset >= 0 and limit >= 0:
                try:
                    sql = '''SELECT * FROM country LIMIT %s, %s'''
                    results = self.dbman.readmany(sql, offset, limit)
                    countries = [self.tocountry(result) for result in results]
                    return countries
                except Exception as e:
                    raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only possitive integer values supported by COUNTRYDAO.RETRIVE_ALL')

    def retrive_next(self, country):
        # print('--> Retriving via CountryDAO')
        if isinstance(country, Country):
            try:
                sql = '''SELECT * FROM country WHERE code>%s ORDER BY code LIMIT 1'''
                result = self.dbman.read(sql, country.country_code)
                return self.tocountry(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only Country Instance values supported by COUNTRYDAO.RETRIVE_NEXT')

    def retrive_previous(self, country):
        # print('--> Retriving via CountryDAO')
        if isinstance(country, Country):
            try:
                sql = '''SELECT * FROM country WHERE code<%s ORDER BY code DESC LIMIT 1'''
                result = self.dbman.read(sql, country.country_code)
                return self.tocountry(result)
            except Exception as e:
                raise ConnectionError('Database Error: {}'.format(e))
        raise ValueError('Only Country Instance values supported by COUNTRYDAO.RETRIVE_PREVIOUS')

    def update(self, country):
        try:
            with self.dbman as db:
                if(self.retrive(country)):
                    sql = '''UPDATE country
                             SET name=%s, continent=%s, region=%s, surface_area=%s,
                             independent_year=%s, population=%s, life_expectation=%s, gnp=%s,
                             gnp_old=%s, local_name=%s, government_form=%s, head_of_state=%s,
                             capital=%s, code2=%s
                             WHERE code=%s'''
                db.write(sql, country.name, country.continent, country.region,
                         country.surface_area, country.independent_year, country.population,
                         country.life_expectation, country.gnp, country.gnp_old,
                         country.local_name, country.government_form, country.head_of_state,
                         country.capital, country.code2, country.country_code)
        except Exception:
            raise ValueError('Only Country Instance values supported by COUNTRYDAO.UPDATE')

    def delete(self, country):
        try:
            with self.dbman as db:
                if(self.retrive(country)):
                    sql = '''DELETE FROM country WHERE code=%s'''
                db.write(sql, country.country_code)
        except Exception:
            raise ValueError('Only Country Instance values supported by COUNTRYDAO.DELETE')

    @staticmethod
    def tocountry(result):
        country_code, name, continent, region, surface_area, independent_year, \
            population, life_expectation, gnp, gnp_old, local_name, \
            government_form, head_of_state, capital, code2 = result
        country = Country(country_code, name, continent, region, surface_area, independent_year,
                          population, life_expectation, gnp, gnp_old, local_name, government_form,
                          head_of_state, capital, code2)
        return country


module_name = 'countries.CountryDAO'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
