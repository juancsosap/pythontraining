# -*- coding:utf-8 -*-

from tools import DAO

from countrieslanguages.countrylanguage import CountryLanguage


class CountryLanguageDAO(DAO):

    def create(self, countrylanguage):
        try:
            with self.dbman as db:
                if(not self.retrive(countrylanguage)):
                    sql = '''INSERT INTO countrylanguage (countrycode, language, district, population)
                             VALUES (%s, %s, %s, %s)'''
                db.write(sql, countrylanguage.country_code, countrylanguage.language,
                         countrylanguage.is_official, countrylanguage.percentage)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    def retrive(self, countrylanguage):
        try:
            with self.dbman as db:
                sql = '''SELECT * FROM countrylanguage WHERE countrycode=%s LIMIT 1'''
                result = db.read(sql, countrylanguage.country_code)
                return self.tocountrylanguage(result)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    def retrive_all(self, offset=0, limit=20):
        try:
            with self.dbman as db:
                sql = '''SELECT * FROM countrylanguage LIMIT $s, %s'''
                results = db.readmany(sql, offset, limit)
                countrieslanguages = [self.tocountrylanguage(result) for result in results]
                return countrieslanguages
        except Exception:
            raise ValueError('Only possitive integer values supported')

    def retrive_next(self, countrylanguage):
        try:
            with self.dbman as db:
                sql = '''SELECT * FROM countrylanguage WHERE countrycode>%s
                         ORDER BY countrycode LIMIT 1'''
                result = db.read(sql, countrylanguage.country_code)
                return self.tocountrylanguage(result)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    def retrive_previous(self, countrylanguage):
        try:
            with self.dbman as db:
                sql = '''SELECT * FROM countrylanguage WHERE countrycode<%s
                         ORDER BY countrycode DESC LIMIT 1'''
                result = db.read(sql, countrylanguage.country_code)
                return self.tocountrylanguage(result)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    def update(self, countrylanguage):
        try:
            with self.dbman as db:
                if(self.retrive(countrylanguage)):
                    sql = '''UPDATE countrylanguage
                             SET language=%s, is_official=%s, percentage=%s
                             WHERE countrycode=%s'''
                db.write(sql, countrylanguage.language, countrylanguage.is_official,
                         countrylanguage.percentage, countrylanguage.country_code)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    def delete(self, countrylanguage):
        try:
            with self.dbman as db:
                if(self.retrive(countrylanguage)):
                    sql = '''DELETE FROM countrylanguage WHERE countrycode=%s'''
                db.write(sql, countrylanguage.country_code)
        except Exception:
            raise ValueError('Only CountryLanguage Instance values supported')

    @staticmethod
    def tocountrylanguage(result):
        country_code, language, district, population = result
        countrylanguage = CountryLanguage(country_code, language, district, population)
        return countrylanguage


module_name = 'countrieslanguages.CountryLanguageDAO'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
