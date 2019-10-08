class Calculator:
    @staticmethod
    def add(n1, n2):
        if(isinstance(n1, float) and isinstance(n2, float)):
            return n1 + n2
        else:
            raise ValueError

    @staticmethod
    def sub(n1, n2):
        if(isinstance(n1, float) and isinstance(n2, float)):
            return n1 - n2
        else:
            raise ValueError

    @staticmethod
    def mul(n1, n2):
        if(isinstance(n1, float) and isinstance(n2, float)):
            return n1 * n2
        else:
            raise ValueError

    @staticmethod
    def div(n1, n2):
        if(isinstance(n1, float) and isinstance(n2, float)):
            return n1 / n2
        else:
            raise ValueError

class CalculatorIntAdapter:
    @staticmethod
    def sumar(n1, n2):
        return int(Calculator.add(float(n1), float(n2)))

    @staticmethod
    def restar(n1, n2):
        return int(Calculator.sub(float(n1), float(n2)))

    @staticmethod
    def multiplicar(n1, n2):
        return int(Calculator.mul(float(n1), float(n2)))

    @staticmethod
    def dividir(n1, n2):
        return int(Calculator.div(float(n1), float(n2)))

class CalculatorStrAdapter:
    @staticmethod
    def sumar(n1, n2):
        return str(Calculator.add(float(n1), float(n2)))

    @staticmethod
    def restar(n1, n2):
        return str(Calculator.sub(float(n1), float(n2)))

    @staticmethod
    def multiplicar(n1, n2):
        return str(Calculator.mul(float(n1), float(n2)))

    @staticmethod
    def dividir(n1, n2):
        return str(Calculator.div(float(n1), float(n2)))

if __name__ == "__main__":
    print('ADD:', CalculatorIntAdapter.sumar(150, 7))
    print('SUB:', CalculatorIntAdapter.restar(150, 7))
    print('MUL:', CalculatorIntAdapter.multiplicar(150, 7))
    print('DIV:', CalculatorIntAdapter.dividir(150, 7))

    print()

    print('ADD:', CalculatorStrAdapter.sumar('150', '7'))
    print('SUB:', CalculatorStrAdapter.restar('150', '7'))
    print('MUL:', CalculatorStrAdapter.multiplicar('150', '7'))
    print('DIV:', CalculatorStrAdapter.dividir('150', '7'))
