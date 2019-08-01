from data import Bit, Byte
from blocks import Adder

def main():
    b1 = Bit(1)
    b2 = Bit(True)
    print(' ', 'not', b1, ':', ~b1)
    print(b1, 'and', b2, ':', b1 & b2)
    print(b1, 'or ', b2, ':', b1 | b2)
    print(b1, 'xor', b2, ':', b1 ^ b2)

    B11 = Byte('10101010')
    B12 = Byte('11111111')
    B21 = Byte('11001100')
    B22 = Byte('11110000')
    B31 = Byte('10100101')
    B32 = Byte('01010101')

    ADD1 = Adder(B11, B12)
    rest1, output1 = ADD1.getrest(), ADD1.getoutput()
    print(' ', B11, sep='')
    print(' ', B12, ' +', sep='')
    print('-----------')
    print(rest1, output1, sep='')

    print()

    ADD2 = Adder(B21, B22, rest1)
    rest2, output2 = ADD2.getrest(), ADD2.getoutput()
    print(' ', B21, ':', B11, sep='')
    print(' ', B22, ':', B12, ' +', sep='')
    print('--------------------')
    print(rest2, output2, ':', output1, sep='')

    print()

    ADD3 = Adder(B31, B32, rest2)
    rest3, output3 = ADD3.getrest(), ADD3.getoutput()
    print(' ', B31, ':', B21, ':', B11, sep='')
    print(' ', B32, ':', B22, ':', B12, ' +', sep='')
    print('-----------------------------')
    print(rest3, output3, ':', output2, ':', output1, sep='')

if __name__ == '__main__':
    main()
