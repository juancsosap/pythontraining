# -*- coding:utf-8 -*-


class Language:

    def __init__(self, language='UND', is_official='F', percentage=0.0):
        self.__language = language
        self.__is_official = is_official
        self.__percentage = percentage

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if(isinstance(value, str)):
            if(len(value) > 2):
                self.__language = value
                return
        raise ValueError(
            'Only larger than 2 characters strings values supported by COUNTRYLANGUAGES.LANGUAGE')

    @property
    def is_official(self):
        return self.__is_official

    @is_official.setter
    def is_official(self, value):
        if(isinstance(value, bool)):
            self.__is_official = value
            return
        raise ValueError('Only boolean values supported by COUNTRYLANGUAGES.IS_OFFICIAL')

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, value):
        if(isinstance(value, float)):
            if(value >= 0.0):
                self.__percentage = value
                return
        raise ValueError('Only possitive float values supported by COUNTRYLANGUAGES.PERCENTAGE')


class CountryLanguages:

    def __init__(self, country_code):
        self.__country_code = country_code
        self.__languages = []

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        if(isinstance(value, str)):
            if(len(value) == 3):
                self.__country_code = value
                return
        raise ValueError(
            'Only 3 characters string values supported by COUNTRYLANGUAGES.COUNTRY_CODE')

    @property
    def languages(self):
        return self.__languages

    def add(self, value):
        if(isinstance(value, Language)):
            self.__languages.append(value)
            return
        raise ValueError('Only Language Instances values supported by COUNTRYLANGUAGES.LANGUAGES')


module_name = 'countrieslanguages.CountryLanguage'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
