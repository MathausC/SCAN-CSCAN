tam = 8
tam_disco = 200


def CSCAN(arr, cabeçote):

    cont_buscas = 0
    distance = 0
    trilha_atual = 0
    esquerda = []
    direita = []
    sequencia_de_busca = []

    esquerda.append(0)
    direita.append(tam_disco - 1)

    for i in range(tam):
        if (arr[i] < cabeçote):
            esquerda.append(arr[i])
        if (arr[i] > cabeçote):
            direita.append(arr[i])

    esquerda.sort()
    direita.sort()

    for i in range(len(direita)):
        trilha_atual = direita[i]

        sequencia_de_busca.append(trilha_atual)

        distance = abs(trilha_atual - cabeçote)

        cont_buscas += distance

        cabeçote = trilha_atual

    cabeçote = 0

    cont_buscas += (tam_disco - 1)

    for i in range(len(esquerda)):
        trilha_atual = esquerda[i]

        sequencia_de_busca.append(trilha_atual)

        distance = abs(trilha_atual - cabeçote)

        cont_buscas += distance

        cabeçote = trilha_atual

    print("Numero total de operações =",
          cont_buscas)
    print("A sequecia de busca é ")
    print(*sequencia_de_busca, sep="\n")

arr = [176, 79, 34, 60,
       92, 11, 41, 114]
cabeçote = 50

print("Posição inicial do cabeçote:", cabeçote)

CSCAN(arr, cabeçote)