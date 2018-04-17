from vector_operations import suma as sumaV


def suma(m1, m2):
    if(isinstance(m1, list) and isinstance(m2, list)):
        if(len(m1) == len(m2)):
            matrix = []
            for (f1, f2) in zip(m1, m2):
                lista = sumaV(f1, f2)
                matrix.append(lista)
            return matrix
        else:
            print("Las listas (matrix) deben contener la misma cantidad de listas (filas)")
            return None
    else:
        print("Los argumentos deben ser listas (matrix)")
        return None
