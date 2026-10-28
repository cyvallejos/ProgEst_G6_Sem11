from arbol_binario import inorden, insertar


def eliminar(raiz, valor):
    if raiz is None:
        return None

    if valor < raiz["valor"]:
        raiz["izq"] = eliminar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = eliminar(raiz["der"], valor)
    elif raiz["izq"] is None:
        return raiz["der"]
    elif raiz["der"] is None:
        return raiz["izq"]
    else:
        sucesor = raiz["der"]
        while sucesor["izq"] is not None:
            sucesor = sucesor["izq"]
        raiz["valor"] = sucesor["valor"]
        raiz["der"] = eliminar(raiz["der"], sucesor["valor"])

    return raiz


def crear_arbol(valores):
    raiz = None
    for valor in valores:
        raiz = insertar(raiz, valor)
    return raiz


if __name__ == "__main__":
    raiz = crear_arbol([50, 30, 70, 20, 40, 60, 80])

    raiz = eliminar(raiz, 20)
    assert inorden(raiz) == [30, 40, 50, 60, 70, 80]

    raiz = eliminar(raiz, 30)
    assert inorden(raiz) == [40, 50, 60, 70, 80]

    raiz = eliminar(raiz, 70)
    assert inorden(raiz) == [40, 50, 60, 80]

    raiz = eliminar(raiz, 50)
    assert inorden(raiz) == [40, 60, 80]
    assert eliminar(None, 5) is None

    print("Eliminacion de hoja, nodo con un hijo y nodos con dos hijos correcta.")
    print("Inorden final:", *inorden(raiz))
