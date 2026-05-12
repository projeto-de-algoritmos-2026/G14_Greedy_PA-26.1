# G14_Greedy_PA-26.1

Número da Dupla: 14<br>
Conteúdo da Disciplina: Greedy<br>
Vídeo da Apresentação: (https://youtu.be/SevDtAX_R6E)

## Alunas
|Matrícula | Aluna |
| -- | -- |
| 231026840 |  Laryssa Félix |
| 231027005  |  Maria Samara |

---

## Sobre 

Este projeto tem como objetivo demonstrar a aplicação prática de algoritmos ambiciosos por meio da implementação do **Algoritmo de Huffman**, utilizado para compactação de dados e codificação eficiente de textos.

A proposta do sistema é mostrar como decisões localmente ótimas podem gerar uma solução global eficiente. No algoritmo de Huffman, os caracteres mais frequentes recebem códigos binários menores, enquanto caracteres menos frequentes recebem códigos maiores, reduzindo a quantidade total de bits necessários para representar uma mensagem.

Além da implementação do algoritmo, o projeto também apresenta uma interface visual interativa desenvolvida com Streamlit, permitindo visualizar todas as etapas da construção da árvore de Huffman, os códigos gerados e as métricas de compressão obtidas.

O sistema busca unir conceitos de:
- Algoritmos Ambiciosos;
- Estruturas de Dados;
- Filas de Prioridade (Min Heap);
- Árvores Binárias;
- Compressão de Dados;
- Visualização Computacional.

---

### Modelagem do Problema

O  problema abordado consiste na compactação eficiente de textos.

Dado um texto de entrada, o sistema deve:
1. Identificar a frequência de ocorrência de cada caractere;
2. Construir uma árvore binária de Huffman;
3. Gerar códigos binários únicos para cada caractere;
4. Codificar o texto original utilizando os códigos gerados;
5. Permitir a decodificação do texto compactado;
6. Comparar o tamanho original e o tamanho compactado da mensagem.

O principal objetivo é minimizar o custo total da representação binária do texto, reduzindo a quantidade de bits utilizados durante o armazenamento ou transmissão da informação.

A estratégia utilizada segue o paradigma ambicioso:
- Em cada etapa, o algoritmo seleciona os dois nós de menor frequência para formar uma nova subárvore;
- Essa escolha localmente ótima contribui para a construção de uma árvore globalmente eficiente.

A modelagem também utiliza:
- Fila de prioridade baseada em Min Heap;
- Estrutura de árvore binária;
- Codificação prefixada, evitando ambiguidades na decodificação.

---

### Algoritmo Utilizado: Huffman

Para resolver o problema, foi utilizado o **algoritmo ambicioso de Huffman**, um algoritmo ambicioso clássico utilizado em sistemas de compressão de dados.

O algoritmo funciona atribuindo códigos binários menores para caracteres mais frequentes e códigos maiores para caracteres menos frequentes. Dessa forma, a quantidade total de bits necessária para representar o texto é reduzida.

A estratégia gulosa utilizada consiste em:
- Analisar a frequência de cada simbolo do texto;
- Selecionar repetidamente os dois nós com menor frequência;

## Justificativa do algoritmo

- Combinar esses nós em uma nova subárvore;
- Inserir novamente essa subárvore na fila de prioridade;
- Repetir o processo até formar a árvore completa.

### Etapas do algoritmo

1. Contagem da frequência dos caracteres;
2. Criação da fila de prioridade (Min Heap);
3. Construção da árvore de Huffman;
4. Geração dos códigos binários;
5. Codificação do texto;
6. Decodificação da mensagem compactada.

### Estruturas de dados utilizadas

- Min Heap;
- Árvore Binária;
- Dicionários;
- Filas de prioridade

### Vantagens do algoritmo

- Alta eficiência de compressão;
- Redução do espaço de armazenamento;
- Decodificação sem ambiguidades;
- Aplicação em sistemas reais de compactação;
- Implementação eficiente utilizando filas de prioridade.

---


## Funcionamento do Sistema

O sistema desenvolvido possui uma interface visual interativa que permite acompanhar todas as etapas do funcionamento do algoritmo.

### O sistema permite:

- Inserir textos personalizados para compactação;
- Calcular automaticamente a frequência dos caracteres;
- Visualizar a tabela de frequências;
- Exibir o passo a passo da estratégia ambiciosa;
- Construir a árvore de Huffman;
- Gerar os códigos binários dos caracteres;
- Codificar automaticamente o texto;
- Decodificar o texto compactado;
- Comparar o tamanho original e o tamanho compactado;
- Calcular métricas de compressão;
- Visualizar gráficos e tabelas interativas;
- Exibir a árvore de Huffman graficamente utilizando Graphviz.

### Interface visual

A interface foi desenvolvida utilizando Streamlit, proporcionando:
- interação em tempo real;
- visualização gráfica;
- organização modular;
- fácil execução e demonstração.

---

## **01 - Caixa de Digitação do Texto**
É preciso pressionar **"Ctrl + Enter"** para enviar o texto digitado.

<img width="953" height="293" alt="image" src="https://github.com/user-attachments/assets/b865d8c1-b8ca-4d1a-85c6-7ca832a47055" />

---

## **02 - Tabela de Frequência dos Caracteres**
Tabela de frequência dos caracteres da palavra **"Universidade"** e o gráfico de barras ilustrando a distribuição das frequências.

<img width="931" height="531" alt="image" src="https://github.com/user-attachments/assets/fdb20765-8621-4bc7-9946-71aee050a2aa" />

---

## **03 - Passo a Passo do Algoritmo e Codificação em Bits**
Tabela contendo o processo de construção gulosa da árvore de Huffman e os códigos binários gerados para cada caractere.

<img width="928" height="566" alt="image" src="https://github.com/user-attachments/assets/0bca01a4-f72e-4d03-9bf8-b231fd92bf99" />

---

## **04 - Árvore de Huffman Gerada**
Árvore de Huffman construída a partir da palavra **"Universidade"**.

<img width="806" height="601" alt="image" src="https://github.com/user-attachments/assets/382ac407-e75d-4bb2-b09a-6495bc1bada6" />

---

## **05 - Codificação, Decodificação e Métricas**
Resultado da codificação e decodificação da palavra **"Universidade"**, além das métricas de compressão obtidas.

<img width="900" height="360" alt="image" src="https://github.com/user-attachments/assets/48d90e20-1fa3-492f-bb5d-1ed6836050fb" />




## Instalação 
<!-- Linguagem: python 3.10+<br>
Framework: Streamlit<br> -->

### Pré-requisitos:


### Passos:

Clone o repositório:
```bash
git clone https://github.com/projeto-de-algoritmos-2026/G14_Grafos_PA-26.1
cd G14_Greedy_PA-26.1
```

Instale as dependências:
```
pip install -r requirements.txt
```

## Uso 

Para executar o projeto, utilize o seguinte comando:
```
streamlit run app.py 
```
### Após executar:

1. O usuário insere um texto;
2. O sistema calcula as frequências dos caracteres;
3. A Min Heap é construída;
4. O algoritmo executa as combinações gulosas;
5. A árvore de Huffman é gerada;
6. Os códigos binários são atribuídos;
7. O texto é compactado;
8. O sistema exibe métricas e resultados visuais.

## Justificativa do algoritmo

O algoritmo ambicioso de Huffman foi escolhido por ser uma solução eficiente e clássica para problemas de compactação de dados. Sua principal característica é a utilização de uma estratégia gulosa, na qual, a cada etapa, são escolhidos os dois caracteres com menor frequência para formar uma nova subárvore.

Essa abordagem permite construir uma árvore binária ótima, reduzindo significativamente a quantidade de bits necessária para representar uma mensagem. Dessa forma, caracteres mais frequentes recebem códigos menores, enquanto caracteres menos frequentes recebem códigos maiores, tornando a codificação mais eficiente.

Além de demonstrar claramente o funcionamento de algoritmos ambiciosos, o Huffman também possibilita a aplicação de importantes conceitos da computação, como:
- Árvores binárias;
- Filas de prioridade (Min Heap);
- Estruturas de dados;
- Compressão de dados;
- Otimização computacional.

O algoritmo também foi escolhido por possuir aplicações reais em sistemas de compressão utilizados no cotidiano, como arquivos ZIP, imagens e transmissão de dados.

Outro fator importante foi a possibilidade de desenvolver uma interface visual interativa, permitindo visualizar:
- A frequência dos caracteres;
- A construção da árvore de Huffman;
- Os códigos binários gerados;
- O processo de codificação e decodificação;
- As métricas de compressão obtidas.

Assim, o projeto consegue unir teoria e prática, demonstrando de forma visual e interativa a eficiência do algoritmo de Huffman e sua importância na área da computação.

## Estrutura do Projeto

```bash
G14_Grafos_PA-26.1 /
projeto_huffman/
│
├── algoritmo/
│   ├── __init__.py
│   ├── huffman.py           # lógica principal do algoritmo;
│   ├── metricas.py          # cálculo de compressão;
│   └── visualizacao.py      # geração da árvore;
|
├── app.py                   # interface Streamlit;
├── requirements.txt
│
└── README.md
