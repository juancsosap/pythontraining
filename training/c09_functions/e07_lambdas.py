import random

pred = lambda x : x > 0
print(pred(5))

cons = lambda msg : print(msg)
cons("hello")

supp = lambda : int(random.random() * 100)
print(supp())

func = lambda text : len(text)
print(func("texto"))


print(type(func))

##########################################


def print_iterable(l):
    print('[ ', end='')
    for d in l:
        print(d, end=' ')
    print(']')


class Collection:
    def __init__(self, *datas):
        self.values = []
        for data in datas:
            self.values.append(data)
    
    def filter(self, predicate):
        result = []
        for data in self.values:
            if(predicate(data)):
                result.append(data)
        return Collection(*result)
        
    def forEach(self, consumer):
        for data in self.values:
            consumer(data)

    def forAll(self, consumer):
        consumer(self.values)


list1 = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 9]

Collection(*list1).forAll(print_iterable)

Collection(*list1).filter(lambda v : v % 2 == 0)\
                  .forAll(print_iterable)

Collection(*list1).filter(lambda v : v % 2 == 0)\
                  .filter(lambda v : v > 5)\
                  .forAll(print_iterable)

print_iterable(map(lambda v : v * v, list1))
    