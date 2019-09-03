class CharAnalizer:
    @staticmethod
    def clean(text):
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = text.replace('\'', ' ')

        return text

    @staticmethod
    def set(text):
        text = CharAnalizer.clean(text)
        chars = set(text)

        return chars

    @staticmethod
    def list(text):
        text = CharAnalizer.clean(text)
        chars = list(text)

        return chars

    @staticmethod
    def count(text):
        text = CharAnalizer.clean(text)
        chars = CharAnalizer.set(text)
        size = len(text)

        return (size, len(chars))
    
    @staticmethod
    def top(text, limit=0, highest=True):
        chars = CharAnalizer.set(text)

        '''
        reg = []
        for c in chars:
            q = 0
            for l in CharAnalizer.list(text):
                if(c == l):
                    q += 1
            reg.append((q, c))
        '''

        reg = dict()
        for c in CharAnalizer.list(text):
            reg[c] = reg.get(c, 0) + 1
        reg = [(q, c) for c, q in reg.items()]

        reg.sort()

        if(highest): reg.reverse()

        size = len(chars)

        if(limit == 0 or limit >= size):
            return reg
        else:
            return reg[:limit]
        

if __name__ == "__main__":
    text = '''
    An aware object has sufficient knowledge of 
    applicable algorithmic and political time 
    adjustments, such as time zone and daylight 
    saving time information, to locate itself 
    relative to other aware objects. An aware 
    object is used to represent a specific moment 
    in time that is not open to interpretation 1.
    
    A naive object does not contain enough 
    information to unambiguously locate itself 
    relative to other date time objects. Whether 
    a naive object represents Coordinated Universal 
    Time , local time, or time in some other timezone
    is purely up to the program, just like it is up 
    to the program whether a particular number 
    represents metres, miles, or mass. Naive 
    objects are easy to understand and to work with,   
       at    ...  . ,         the cost of ignoring some aspects of reality.
    '''

    result1, result2 = CharAnalizer.count(text)
    print(result1)
    print(result2)

    result3 = CharAnalizer.top(text, 10, False)
    print(result3)