def quebrar_vigenere_ingles(cifrado, tamanho_chave):
    # Frequência estatística aproximada das letras no idioma inglês
    freq_en = [0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 
               0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 
               0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 
               0.0197, 0.0007]
    
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave = ""

    # Análise de frequência para cada coluna do texto
    for i in range(tamanho_chave):
        coluna = cifrado[i::tamanho_chave]
        melhor_shift = 0
        menor_erro = float('inf')

        for shift in range(26):
            erro = 0
            for letra in range(26):
                letra_cifrada = alfabeto[(letra + shift) % 26]
                contagem = coluna.count(letra_cifrada)
                freq_observada = contagem / len(coluna)
                freq_esperada = freq_en[letra]
                
                # Teste de qui-quadrado
                if freq_esperada > 0:
                    erro += ((freq_observada - freq_esperada) ** 2) / freq_esperada
            
            if erro < menor_erro:
                menor_erro = erro
                melhor_shift = shift
                
        chave += alfabeto[melhor_shift]

    print(f"Chave provável encontrada: {chave}")
    
    texto_claro = ""
    for i, char in enumerate(cifrado):
        shift = alfabeto.index(chave[i % tamanho_chave])
        char_idx = alfabeto.index(char)
        texto_claro += alfabeto[(char_idx - shift) % 26]

    print(f"\nTexto decifrado: \n{texto_claro}")

cifrado = (
    "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUD"
    "DKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYC"
    "QKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRL"
    "SVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMV"
    "GKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFS"
    "PEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHI"
    "FFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIY"
    "CWHJVLNHIQIBTKHJVNPIST"
)

quebrar_vigenere_ingles(cifrado, 6)