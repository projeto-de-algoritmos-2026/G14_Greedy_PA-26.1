import heapq
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Tuple


@dataclass(order=True)
class NoHuffman:
    frequencia: int
    ordem: int
    caractere: Optional[str] = field(compare=False, default=None)
    esquerda: Optional["NoHuffman"] = field(compare=False, default=None)
    direita: Optional["NoHuffman"] = field(compare=False, default=None)

    def eh_folha(self) -> bool:
        return self.caractere is not None


def calcular_frequencias(texto: str) -> Counter:
    return Counter(texto)


def rotulo_no(no: NoHuffman) -> str:
    if no.eh_folha():
        return f"{repr(no.caractere)}({no.frequencia})"
    return f"Subárvore({no.frequencia})"


def construir_arvore_huffman(
    texto: str
) -> Tuple[Optional[NoHuffman], List[Dict]]:

    frequencias = calcular_frequencias(texto)

    heap: List[NoHuffman] = []

    passos = []

    ordem = 0

    for caractere, frequencia in frequencias.items():

        heapq.heappush(
            heap,
            NoHuffman(
                frequencia,
                ordem,
                caractere
            )
        )

        ordem += 1

    if not heap:
        return None, passos

    passo = 1

    while len(heap) > 1:

        no1 = heapq.heappop(heap)

        no2 = heapq.heappop(heap)

        novo_no = NoHuffman(
            frequencia=no1.frequencia + no2.frequencia,
            ordem=ordem,
            caractere=None,
            esquerda=no1,
            direita=no2
        )

        ordem += 1

        heapq.heappush(heap, novo_no)

        passos.append({
            "Passo": passo,
            "Nó 1": rotulo_no(no1),
            "Nó 2": rotulo_no(no2),
            "Resultado": rotulo_no(novo_no)
        })

        passo += 1

    return heap[0], passos


def gerar_codigos(
    no,
    codigo_atual="",
    codigos=None
):

    if codigos is None:
        codigos = {}

    if no is None:
        return codigos

    if no.eh_folha():

        codigos[
            no.caractere
        ] = codigo_atual or "0"

    gerar_codigos(
        no.esquerda,
        codigo_atual + "0",
        codigos
    )

    gerar_codigos(
        no.direita,
        codigo_atual + "1",
        codigos
    )

    return codigos


def codificar_texto(
    texto,
    codigos
):

    return "".join(
        codigos[caractere]
        for caractere in texto
    )


def decodificar_texto(
    texto_codificado,
    raiz
):

    resultado = ""

    no_atual = raiz

    for bit in texto_codificado:

        if bit == "0":
            no_atual = no_atual.esquerda

        else:
            no_atual = no_atual.direita

        if no_atual.eh_folha():

            resultado += no_atual.caractere

            no_atual = raiz

    return resultado