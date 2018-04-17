class Contact:
    def __init__(self, name, **kargs):
        self.name = name
        for key in kargs:
            self.__dict__[key] = kargs[key]

    def addPhones(self, *phones):
        if 'phone' in self.__dict__:
            if type(self.phone) != type(list):
                self.phone = [self.phone]
        for phone in phones:
            self.phone.append(phone)

    def __str__(self):
        text = ''
        for key, value in self.__dict__.items():
            text += f'{key.capitalize()}:\t{value}\n'
        return text


if __name__ == '__main__':
    juan = Contact('Juan Sosa', phone='+56 9 4632 7016', address='Huechuraba')
    print(juan)
    print()
    juan.addPhones('12345678', '987654321')
    print(juan)
