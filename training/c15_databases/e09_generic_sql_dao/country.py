class Country:
    def __init__(self, code, name, continent):
        self.code = code
        self.name = name
        self.continent = continent
    
    def __str__(self):
        return '{code:>5} : {name:30} {continent:15}'.format(**self.__dict__)
