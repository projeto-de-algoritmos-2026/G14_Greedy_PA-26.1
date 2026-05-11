from typing import Optional
from graphviz import Digraph
from algoritmo.huffman import NoHuffman


def imprimir_arvore(
    no: Optional[NoHuffman],
    nivel: int = 0,
    lado: str = "Raiz"
) -> None:

    if no is None:
        return

    indentacao = "   " * nivel

    if no.eh_folha():
        print(
            f"{indentacao}[{lado}] "
            f"'{no.caractere}' "
            f"(freq={no.frequencia})"
        )
    else:
        print(
            f"{indentacao}[{lado}] "
            f"Subárvore "
            f"(freq={no.frequencia})"
        )

    imprimir_arvore(no.esquerda, nivel + 1, "0")
    imprimir_arvore(no.direita, nivel + 1, "1")


def imprimir_codigos(codigos: dict) -> None:

    print("\nCódigos de Huffman:\n")

    for caractere, codigo in sorted(codigos.items()):
        print(f"{repr(caractere)} -> {codigo}")


def gerar_graphviz(raiz: NoHuffman):

    dot = Digraph()

    def adicionar_nos(no, pai=None, lado=""):

        if no is None:
            return

        node_id = str(id(no))

        if no.eh_folha():
            label = f"{repr(no.caractere)}\n{no.frequencia}"
        else:
            label = f"{no.frequencia}"

        dot.node(node_id, label)

        if pai:
            dot.edge(pai, node_id, label=lado)

        adicionar_nos(no.esquerda, node_id, "0")
        adicionar_nos(no.direita, node_id, "1")

    adicionar_nos(raiz)

    return dot