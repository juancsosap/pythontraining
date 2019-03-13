def resta(l1, l2):
    if(isinstance(l1, list) and isinstance(l2, list)):
        if(len(l1) == len(l2)):
            lista = []
            for (v1, v2) in zip(l1, l2):
                if(type(v1) == type(v2)):
                    lista.append(v1 - v2)
                else:
                    print("Los valores deben ser del mismo tipo")
                    return None
            return lista
        else:
            print("Las listas deben contener la misma cantidad de elementos")
            return None
    else:
        print("Los argumentos deben ser listas")
        return None
