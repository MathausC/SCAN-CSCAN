tam = 8
tam_disco = 200
 
def SCAN(arr, cabeçote, direcao):
 
    cont_buscas = 0
    distancia, trilha_atual = 0, 0
    esquerda = []
    direita = []
    sequencia_de_busca = []
 
    if (direcao == "esquerda"):
        esquerda.append(0)
    elif (direcao == "direita"):
        direita.append(tam_disco - 1)
 
    for i in range(tam):
        if (arr[i] < cabeçote):
            esquerda.append(arr[i])
        if (arr[i] > cabeçote):
            direita.append(arr[i])
 
    esquerda.sort()
    direita.sort()
 
    run = 2
    while (run != 0):
        if (direcao == "esquerda"):
            for i in range(len(esquerda) - 1, -1, -1):
                trilha_atual = esquerda[i]
 
                
                sequencia_de_busca.append(trilha_atual)
 
                
                distancia = abs(trilha_atual - cabeçote)
 
                
                cont_buscas += distancia
 
                
                cabeçote = trilha_atual
             
            direcao = "direita"
     
        elif (direcao == "direita"):
            for i in range(len(direita)):
                trilha_atual = direita[i]
                 
                
                sequencia_de_busca.append(trilha_atual)
 
                
                distancia = abs(trilha_atual - cabeçote)
 
                
                cont_buscas += distancia
 
                
                cabeçote = trilha_atual
             
            direcao = "esquerda"
         
        run -= 1
 
    print("Numero total de operações =",
          cont_buscas)
 
    print("A sequecia de busca é ")
 
    for i in range(len(sequencia_de_busca)):
        print(sequencia_de_busca[i])
 

arr = [ 176, 79, 34, 60,
         92, 11, 41, 114 ]
cabeçote = 50
direcao = "esquerda"
 
SCAN(arr, cabeçote, direcao)