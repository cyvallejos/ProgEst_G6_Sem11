def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}


def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)

    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)

    return raiz


def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz["valor"] == valor:
        return True
    if valor < raiz["valor"]:
        return buscar(raiz["izq"], valor)
    return buscar(raiz["der"], valor)


def inorden(raiz):
    """Visita primero el subárbol izquierdo, luego la raíz y después el derecho."""
    if raiz is None:
        return []
    return inorden(raiz["izq"]) + [raiz["valor"]] + inorden(raiz["der"])


def preorden(raiz):
    """Visita la raíz, luego el subárbol izquierdo y finalmente el derecho."""
    if raiz is None:
        return []
    return [raiz["valor"]] + preorden(raiz["izq"]) + preorden(raiz["der"])


def postorden(raiz):
    """Visita los subárboles izquierdo y derecho antes de visitar la raíz."""
    if raiz is None:
        return []
    return postorden(raiz["izq"]) + postorden(raiz["der"]) + [raiz["valor"]]


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])


def altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))


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


if __name__ == "__main__":
    raiz = None
    for numero in [50, 30, 70, 20, 40, 60, 80]:
        raiz = insertar(raiz, numero)

    print(buscar(raiz, 60))
    print(*inorden(raiz))
    print(*preorden(raiz))
    print(*postorden(raiz))
    print(f"Numero de nodos: {contar_nodos(raiz)}")
    print(f"Altura: {altura(raiz)}")
