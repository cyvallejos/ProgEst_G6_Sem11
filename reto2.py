from arbol_binario import insertar


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])


def contar_hojas(raiz):
    if raiz is None:
        return 0
    if raiz["izq"] is None and raiz["der"] is None:
        return 1
    return contar_hojas(raiz["izq"]) + contar_hojas(raiz["der"])


def altura(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))


def crear_arbol(valores):
    raiz = None
    for valor in valores:
        raiz = insertar(raiz, valor)
    return raiz


if __name__ == "__main__":
    arbol_vacio = None
    arbol_un_nodo = crear_arbol([10])
    arbol_ejemplo = crear_arbol([50, 30, 70, 20, 40, 60, 80])

    assert (contar_nodos(arbol_vacio), contar_hojas(arbol_vacio), altura(arbol_vacio)) == (0, 0, -1)
    assert (contar_nodos(arbol_un_nodo), contar_hojas(arbol_un_nodo), altura(arbol_un_nodo)) == (1, 1, 0)
    assert (contar_nodos(arbol_ejemplo), contar_hojas(arbol_ejemplo), altura(arbol_ejemplo)) == (7, 4, 2)

    print("Arbol vacio: nodos=0, hojas=0, altura=-1")
    print("Un nodo: nodos=1, hojas=1, altura=0")
    print("Ejemplo: nodos=7, hojas=4, altura=2")
