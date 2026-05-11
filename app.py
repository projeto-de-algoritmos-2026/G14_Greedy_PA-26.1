import pandas as pd
import streamlit as st
from algoritmo.metricas import calcular_metricas
from algoritmo.visualizacao import gerar_graphviz

from algoritmo.huffman import (
    calcular_frequencias,
    construir_arvore_huffman,
    gerar_codigos,
    codificar_texto,
    decodificar_texto,
)

st.set_page_config(
    page_title="Algoritmo de Huffman",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Compactação de Texto com Huffman")

st.write(
    "Aplicação de um algoritmo ambicioso para compressão de textos."
)

texto = st.text_area(
    "Digite um texto:",
    value="algoritmos ambiciosos"
)

if texto:
    raiz, passos = construir_arvore_huffman(texto)

    codigos = gerar_codigos(raiz)

    texto_codificado = codificar_texto(texto, codigos)

    texto_decodificado = decodificar_texto(texto_codificado, raiz)

    metricas = calcular_metricas(texto, texto_codificado)

    frequencias = calcular_frequencias(texto)

    st.header("Tabela de Frequências")

    df_freq = pd.DataFrame([
        {
            "Caractere": caractere,
            "Frequência": frequencia
        }
        for caractere, frequencia in frequencias.items()
    ])

    df_freq = df_freq.sort_values(
         by="Frequência",
        ascending=True
    ).reset_index(drop=True)

    df_freq.index = df_freq.index + 1

    st.dataframe(df_freq, use_container_width=True)

    st.bar_chart(df_freq.set_index("Caractere")["Frequência"])

    st.header("Passo a passo guloso")

    # st.dataframe(pd.DataFrame(passos), use_container_width=True)

    df_passos = pd.DataFrame(passos)

    df_passos.index = df_passos.index + 1

    st.dataframe(
        df_passos,
        use_container_width=True
    )
    st.header("Códigos Huffman")

    df_codigos = pd.DataFrame([
        {
            "Caractere": caractere,
            "Código": codigo,
            "Tamanho": len(codigo)
        }
        for caractere, codigo in codigos.items()
    ])

    df_codigos = df_codigos.reset_index(drop=True)

    df_codigos.index = df_codigos.index + 1

    st.dataframe(df_codigos, use_container_width=True)

    st.header("Árvore de Huffman")

    st.graphviz_chart(gerar_graphviz(raiz), use_container_width=True)

    st.header("Codificação")

    st.code(texto_codificado)

    st.header("Decodificação")

    st.code(texto_decodificado)

    st.header("Métricas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Bits Originais",
            metricas["Bits Originais"]
        )

    with col2:
        st.metric(
            "Bits Comprimidos",
            metricas["Bits Comprimidos"]
        )

    with col3:
        st.metric(
            "Economia de espaço",
            f"{metricas['Economia (%)']:.2f}%"
        )