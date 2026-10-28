from arbol_binario import buscar, eliminar, inorden, insertar


def registrar(raiz, codigo):
    return insertar(raiz, codigo)


def consultar(raiz, codigo):
    return buscar(raiz, codigo)


def listar_ordenadamente(raiz):
    return inorden(raiz)


def retirar(raiz, codigo):
    return eliminar(raiz, codigo)


if __name__ == "__main__":
    catalogo = None
    for codigo in [1042, 1018, 1095, 1003, 1031, 1070, 1120]:
        catalogo = registrar(catalogo, codigo)

    assert consultar(catalogo, 1031)
    assert not consultar(catalogo, 9999)
    assert listar_ordenadamente(catalogo) == [
        1003, 1018, 1031, 1042, 1070, 1095, 1120
    ]
    catalogo = retirar(catalogo, 1042)
    assert listar_ordenadamente(catalogo) == [
        1003, 1018, 1031, 1070, 1095, 1120
    ]

    catalogo_ascendente = None
    for codigo in [10, 20, 30, 40, 50]:
        catalogo_ascendente = registrar(catalogo_ascendente, codigo)
    assert listar_ordenadamente(catalogo_ascendente) == [10, 20, 30, 40, 50]

    print("Codigos ordenados:", *listar_ordenadamente(catalogo))
    
#Insertar codigos en orden ascendente desequilibra el ABB y lo convierte
#en una cadena; buscar, insertar y retirar pueden degradarse de O(log n)
#a O(n), y la recursion profunda puede exceder el limite de Python.
