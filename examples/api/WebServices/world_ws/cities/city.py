# -*- coding:utf-8 -*-


class City:

    def __init__(self, city_id, name='UND', country_code='UND', district='UND', population=0):
        self.__city_id = city_id
        self.__name = name
        self.__country_code = country_code
        self.__district = district
        self.__population = population

    @property
    def city_id(self):
        return self.__city_id

    @city_id.setter
    def city_id(self, value):
        if(isinstance(value, int)):
            if(value > 0):
                self.__city_id = value
                return
        raise ValueError('Only possitive integer values supported by CITY.CITY_ID')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__name = value
                return
        raise ValueError('Only larger than 2 characters strings values supported by CITY.NAME')

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        if(isinstance(value, str)):
            if(len(value) == 3):
                self.__country_code = value
                return
        raise ValueError('Only 3 characters string values supported by CITY.COUNTRY_CODE')

    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__district = value
                return
        raise ValueError('Only larger than 2 characters strings values supported by CITY.DISTRICT')

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if(isinstance(value, int)):
            if(value >= 0):
                self.__population = value
                return
        raise ValueError('Only possitive integer values supported by CITY.POPULATION')

    def __eq__(self, other):
        if isinstance(other, City):
            return (self.city_id, self.name, self.country_code, self.district, self.population) == \
                   (other.city_id, other.name, other.country_code, other.district, other.population)
        return False

    def __str__(self):
        msg = '{}: {} - {} ({}) [{}]'
        return msg.format(self.city_id, self.name, self.country_code, self.district, self.population)


module_name = 'cities.City'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
