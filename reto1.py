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


def crear_arbol_ejemplo():
    raiz = {"valor": 50, "izq": None, "der": None}
    raiz["izq"] = {"valor": 30, "izq": None, "der": None}
    raiz["izq"]["izq"] = {"valor": 20, "izq": None, "der": None}
    raiz["izq"]["der"] = {"valor": 40, "izq": None, "der": None}
    raiz["der"] = {"valor": 70, "izq": None, "der": None}
    raiz["der"]["izq"] = {"valor": 60, "izq": None, "der": None}
    raiz["der"]["der"] = {"valor": 80, "izq": None, "der": None}
    return raiz


if __name__ == "__main__":
    raiz = crear_arbol_ejemplo()
    recorrido_preorden = preorden(raiz)
    recorrido_postorden = postorden(raiz)

    assert recorrido_preorden[0] == 50
    assert recorrido_postorden[-1] == 50
    assert preorden(None) == []
    assert postorden(None) == []

    print("Preorden (raíz, izquierdo, derecho):", *recorrido_preorden)
    print("Postorden (izquierdo, derecho, raíz):", *recorrido_postorden)
