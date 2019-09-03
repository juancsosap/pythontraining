import re

class WordAnalizer:
    @staticmethod
    def clean(text):
        regex_str = r'~(\d|\w)'
        text = re.sub(regex_str, ' ', text.lower())
        #text = text.lower().replace('\n', ' ') \
        #           .replace(',', '').replace('.', '')
        
        return text

    @staticmethod
    def set(text):
        split_text = WordAnalizer.list(text)
        words = set(split_text)

        return words

    @staticmethod
    def list(text):
        text = WordAnalizer.clean(text)
        
        split_text = text.split(' ')
        split_text.sort()
        split_text.reverse()
        split_text = split_text[:split_text.index('')]
        
        return split_text

    @staticmethod
    def count(text):
        text = WordAnalizer.clean(text)
        words = WordAnalizer.set(text)

        split_text = WordAnalizer.list(text)
        size = len(split_text)

        return (size, len(words))

    @staticmethod
    def top(text, limit=0, highest=True):
        words = WordAnalizer.set(text)
        
        '''
        reg = []
        for w in words:
            q = 0
            for t in WordAnalizer.list(text):
                if(w == t):
                    q += 1
            reg.append((q, c))
        '''

        reg = dict()
        for w in WordAnalizer.list(text):
            reg[w] = reg.get(w, 0) + 1
        reg = [(q, w) for w, q in reg.items()]

        reg.sort()

        if(highest): reg.reverse()

        size = len(words)

        if(limit == 0 or limit >= size):
            return reg
        else:
            return reg[:limit]
    
    @staticmethod
    def length(text, limit=0, highest=True):
        words = WordAnalizer.set(text)

        reg = [(len(w), w) for w in words]

        reg.sort()

        if(highest): reg.reverse()

        size = len(words)

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

    result1, result2 = WordAnalizer.count(text)
    print(result1)
    print(result2)

    result3 = WordAnalizer.top(text, 10)
    print(result3)

    result4 = WordAnalizer.length(text, 10)
    print(result4)

