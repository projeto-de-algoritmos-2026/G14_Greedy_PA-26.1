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


def construir_arvore_huffman(texto: str) -> Tuple[Optional[NoHuffman], List[Dict]]:
    frequencias = calcular_frequencias(texto)

    heap: List[NoHuffman] = []
    passos = []
    ordem = 0

    for caractere, frequencia in frequencias.items():
        heapq.heappush(heap, NoHuffman(frequencia, ordem, caractere))
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
    return "".join(resultado)