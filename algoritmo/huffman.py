import heapq
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Tuple


# Classe que representa um nó da árvore de Huffman
@dataclass(order=True)
class NoHuffman:

    frequencia: int

    ordem: int

    caractere: Optional[str] = field(compare=False, default=None)

    # Filho da esquerda
    esquerda: Optional["NoHuffman"] = field(compare=False, default=None)

    # Filho da direita
    direita: Optional["NoHuffman"] = field(compare=False, default=None)

    # Verifica se o nó é folha
    # Um nó folha possui caractere associado
    def eh_folha(self) -> bool:
        return self.caractere is not None


# Calcula a frequência de cada caractere no texto
def calcular_frequencias(texto: str) -> Counter:

    return Counter(texto)

def rotulo_no(no: NoHuffman) -> str:

    if no.eh_folha():
        return f"{repr(no.caractere)}({no.frequencia})"

    return f"Subárvore({no.frequencia})"


# Constrói a árvore de Huffman
def construir_arvore_huffman(
    texto: str
) -> Tuple[Optional[NoHuffman], List[Dict]]:

    # Calcula frequências dos caracteres
    frequencias = calcular_frequencias(texto)

    # Min Heap usada para selecionar os menores nós
    heap: List[NoHuffman] = []

    passos = []

    ordem = 0

    # Cria um nó para cada caractere
    for caractere, frequencia in frequencias.items():

        # Insere o nó na Min Heap
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

        # Remove os dois nós de menor frequência
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)

        # Cria um novo nó combinando os dois menores
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


# Gera os códigos binários dos caracteres
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

    # Percorre a subárvore esquerda adicionando 0
    gerar_codigos(
        no.esquerda,
        codigo_atual + "0",
        codigos
    )

    # Percorre a subárvore direita adicionando 1
    gerar_codigos(
        no.direita,
        codigo_atual + "1",
        codigos
    )

    return codigos


# Codifica o texto usando os códigos de Huffman
def codificar_texto(
    texto,
    codigos
):

    # Substitui cada caractere pelo código binário correspondente
    return "".join(
        codigos[caractere]
        for caractere in texto
    )


# Decodifica o texto binário usando a árvore de Huffman
def decodificar_texto(
    texto_codificado,
    raiz
):

    # Texto final reconstruído
    resultado = ""

    # Começa na raiz da árvore
    no_atual = raiz

    # Percorre cada bit do texto codificado
    for bit in texto_codificado:

        # Se bit for 0, vai para esquerda
        if bit == "0":
            no_atual = no_atual.esquerda

        # Se bit for 1, vai para direita
        else:
            no_atual = no_atual.direita

        # Quando chegar em uma folha
        if no_atual.eh_folha():

            resultado += no_atual.caractere

            no_atual = raiz

    return resultado