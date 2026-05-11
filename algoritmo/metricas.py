from typing import Dict, Optional
from algoritmo.huffman import NoHuffman


def gerar_codigos(
    no: Optional[NoHuffman],
    codigo_atual: str = "",
    codigos: Optional[Dict[str, str]] = None
) -> Dict[str, str]:

    if codigos is None:
        codigos = {}

    if no is None:
        return codigos

    if no.eh_folha():
        codigos[no.caractere] = codigo_atual or "0"
        return codigos

    gerar_codigos(no.esquerda, codigo_atual + "0", codigos)
    gerar_codigos(no.direita, codigo_atual + "1", codigos)

    return codigos


def codificar_texto(texto: str, codigos: Dict[str, str]) -> str:
    return "".join(codigos[caractere] for caractere in texto)


def calcular_taxa_compressao(texto_original: str, texto_codificado: str) -> float:

    if len(texto_original) == 0:
        return 0

    bits_original = len(texto_original) * 8
    bits_comprimido = len(texto_codificado)

    taxa = (
        (bits_original - bits_comprimido)
        / bits_original
    ) * 100

    return taxa


def calcular_bits_originais(texto: str) -> int:
    return len(texto) * 8


def calcular_bits_comprimidos(texto_codificado: str) -> int:
    return len(texto_codificado)

def calcular_metricas(
    texto_original: str,
    texto_codificado: str
):

    bits_originais = len(texto_original) * 8

    bits_comprimidos = len(texto_codificado)

    economia = (
        (
            bits_originais - bits_comprimidos
        )
        / bits_originais
    ) * 100 if bits_originais > 0 else 0

    return {
        "Bits Originais": bits_originais,
        "Bits Comprimidos": bits_comprimidos,
        "Economia (%)": economia
    }