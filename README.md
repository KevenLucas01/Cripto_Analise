# Vigenère CryptoAnalyzer 🔐

## 📌 Sobre o Projeto
Este repositório contém a implementação de um pipeline de criptoanálise automatizada para a **Cifra de Vigenère**. O algoritmo foi projetado para quebrar textos cifrados complexos através de inspeção heurística e análise estatística orientada a dados, eliminando a necessidade de força bruta exaustiva (tentativa e erro) ou do conhecimento prévio da chave criptográfica.

A solução foi inicialmente desenvolvida como um desafio para a disciplina de Criptografia na Universidade de Brasília (UnB), onde a modelagem matemática adotada provou ser robusta o suficiente para quebrar um texto original em inglês utilizando apenas a matriz de probabilidades da língua portuguesa.

## ⚙️ Arquitetura da Solução

O algoritmo opera fundamentado em três pilares analíticos sucessivos:

1. **Inspeção Heurística (Método de Kasiski):** O script varre o ciphertext em busca de sequências de caracteres repetidas. Ao registrar as distâncias entre essas repetições, o algoritmo calcula o **Máximo Divisor Comum (MDC)** para inferir com alta probabilidade o comprimento exato da chave.

2. **Decomposição Polialfabética:** Com o tamanho da chave descoberto, o texto é fatiado em colunas. Isso reduz o problema original — uma cifra polialfabética complexa — a múltiplos vetores de ataque mais simples, tratando cada coluna como uma Cifra de César independente.

3. **Criptoanálise Estatística (Qui-Quadrado / $\chi^2$):** Para descobrir a letra da chave correspondente a cada vetor, o algoritmo aplica o teste de aderência do Qui-Quadrado. Ele testa todos os 26 deslocamentos possíveis e compara a distribuição de frequência resultante com a matriz de probabilidade do idioma alvo. O menor valor de $\chi^2$ indica o deslocamento correto.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Abordagem:** Análise de Frequência, Estatística Descritiva e Algoritmos de Busca.
- *Não requer bibliotecas externas (construído com a biblioteca padrão do Python para garantir portabilidade).*

## 💻 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/KevenLucas01/Cripto_Analise.git
