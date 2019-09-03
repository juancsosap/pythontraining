class Matrix:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22
    
    def __str__(self):
        return '| {a11:5} {a12:5} |\n| {a21:5} {a22:5} |'.format(a11=self.a11, a12=self.a12, a21=self.a21, a22=self.a22)
    
    def __add__(self, other):
        if(isinstance(other, Matrix)):
            a11 = self.a11 + other.a11
            a12 = self.a12 + other.a12
            a21 = self.a21 + other.a21
            a22 = self.a22 + other.a22
            return Matrix(a11, a12, a21, a22)
        else:
            raise ValueError
    
    def __sub__(self, other):
        if(isinstance(other, Matrix)):
            a11 = self.a11 - other.a11
            a12 = self.a12 - other.a12
            a21 = self.a21 - other.a21
            a22 = self.a22 - other.a22
            return Matrix(a11, a12, a21, a22)
        else:
            raise ValueError
    
    def det(self):
        return self.a11 * self.a22 - self.a12 * self.a21
    
    @staticmethod
    def identity():
        return Matrix(1,0,0,1)

if __name__ == '__main__':
    m1 = Matrix(10,2,300,4)
    print(m1)
    print('+'.center(20))
    m2 = Matrix(100,20,30,400)
    print(m2)
    print('-'*20)
    m3 = m1 + m2
    print(m3)

    print('\n\n')

    print(m1)
    print('-'.center(20))
    print(m2)
    print('-'*20)
    m4 = m1 - m2
    print(m4)

    print('\n\n')

    print(m1.det())

    m5 = Matrix.identity()
    print(m5)

else:
    print('Loading Matrix module')