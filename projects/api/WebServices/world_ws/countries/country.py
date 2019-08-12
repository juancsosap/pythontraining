# -*- coding:utf-8 -*-


class Country:

    def __init__(self, country_code, name='UND', continent='UND', region='UND', surface_area=0.0,
                 independent_year=2000, population=0, life_expectation=0.0, gnp=0.0, gnp_old=0.0,
                 local_name='UND', government_form='UND', head_of_state='UND', capital=0,
                 code2='UND'):
        self.__country_code = country_code
        self.__name = name
        self.__continent = continent
        self.__region = region
        self.__surface_area = surface_area,
        self.__independent_year = independent_year
        self.__population = population
        self.__life_expectation = life_expectation
        self.__gnp = gnp
        self.__gnp_old = gnp_old,
        self.__local_name = local_name
        self.__government_form = government_form
        self.__head_of_state = head_of_state
        self.__capital = capital
        self.__code2 = code2

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        if(isinstance(value, str)):
            if(len(value) == 3):
                self.__country_code = value
                return
        raise ValueError('Only 3 characters string values supported by COUNTRY.COUNTRY_CODE')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__name = value
                return
        raise ValueError('Only larger than 2 characters strings values supported by COUNTRY.NAME')

    @property
    def continent(self):
        return self.__continent

    @continent.setter
    def continent(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__continent = value
                return
        raise ValueError(
            'Only larger than 2 characters strings values supported by COUNTRY.CONTINENT')

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__region = value
                return
        raise ValueError('Only larger than 2 characters strings values supported by COUNTRY.REGION')

    @property
    def surface_area(self):
        return self.__surface_area

    @surface_area.setter
    def surface_area(self, value):
        if(isinstance(value, float)):
            if(value >= 0.0):
                self.__surface_area = value
                return
        raise ValueError('Only possitive float values supported by COUNTRY.SURFACE_AREA')

    @property
    def independent_year(self):
        return self.__independent_year

    @independent_year.setter
    def independent_year(self, value):
        if(isinstance(value, int)):
            if(value > 1000 and value < 2000):
                self.__independent_year = value
                return
        raise ValueError(
            'Only integer values between 1000 and 2000 are supported by COUNTRY.INDEPENDENT_YEAR')

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if(isinstance(value, int)):
            if(value >= 0):
                self.__population = value
                return
        raise ValueError('Only possitive integer values supported by COUNTRY.POPULATION')

    @property
    def life_expectation(self):
        return self.__life_expectation

    @life_expectation.setter
    def life_expectation(self, value):
        if(isinstance(value, float)):
            if(value >= 0.0):
                self.__life_expectation = value
                return
        raise ValueError('Only possitive float values supported by COUNTRY.LIFE_EXPECTATION')

    @property
    def gnp(self):
        return self.__gnp

    @gnp.setter
    def gnp(self, value):
        if(isinstance(value, float)):
            if(value >= 0.0):
                self.__gnp = value
                return
        raise ValueError('Only possitive float values supported by COUNTRY.GNP')

    @property
    def gnp_old(self):
        return self.__gnp_old

    @gnp_old.setter
    def gnp_old(self, value):
        if(isinstance(value, float)):
            if(value >= 0.0):
                self.__gnp_old = value
                return
        raise ValueError('Only possitive float values supported by COUNTRY.GNP_OLD')

    @property
    def local_name(self):
        return self.__local_name

    @local_name.setter
    def local_name(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__local_name = value
                return
        raise ValueError(
            'Only larger than 2 characters strings values supported by COUNTRY.LOCAL_NAME')

    @property
    def government_form(self):
        return self.__government_form

    @government_form.setter
    def government_form(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__government_form = value
                return
        raise ValueError(
            'Only larger than 2 characters strings values supported by COUNTRY.GOVERNMENT_FORM')

    @property
    def head_of_state(self):
        return self.__head_of_state

    @head_of_state.setter
    def head_of_state(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__head_of_state = value
                return
        raise ValueError(
            'Only larger than 2 characters strings values supported by COUNTRY.HEAD_OF_STATE')

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, value):
        if(isinstance(value, int)):
            if(value >= 0):
                self.__capital = value
                return
        raise ValueError('Only possitive integer values supported by COUNTRY.CAPITAL')

    @property
    def code2(self):
        return self.__code2

    @code2.setter
    def code2(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__code2 = value
                return
        raise ValueError('Only larger than 2 characters strings values supported by COUNTRY.CODE2')

    def __eq__(self, other):
        if isinstance(other, Country):
            return (self.country_code, self.name, self.continent, self.region, self.surface_area,
                    self.independent_year, self.population, self.life_expectation, self.gnp,
                    self.gnp_old, self.local_name, self.government_form, self.head_of_state,
                    self.capital, self.code2) == \
                (other.country_code, other.name, other.continent, other.region,
                    other.surface_area, other.independent_year, other.population,
                    other.life_expectation, other.gnp, other.gnp_old, other.local_name,
                    other.government_form, other.head_of_state, other.capital, other.code2)
        return False

    def __str__(self):
        msg = '{}: {} - {} ({}) [{}]'
        return msg.format(self.country_code, self.name, self.continent, self.region, self.population)


module_name = 'countries.Country'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
