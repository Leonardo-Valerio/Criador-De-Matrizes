
def criar_matriz(tam_linha,tam_coluna):
    matriz = []
    for i in range(tam_linha):
        linha = []
        for j in range(tam_coluna):
            elemento = int(input('digite um elemento da matriz: '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def imprimir_matiz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor,end=' ')
        print()

def somar_matriz(matriz1,matriz2):
    matriz3=[]
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        matriz3.append(linha)
    return matriz3

def multi(matriz1,matriz2):
    matriz3 = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            soma = 0
            for k in range(len(matriz1[j])):
                soma += matriz1[i][k] * matriz2[k][j]
            linha.append(soma)
        matriz3.append(linha)
    return matriz3



tamanho_linha = int(input('quantas linhas vc quer? '))
tamanho_coluna = int(input('quantas colunas vc quer? '))

matriz1 = criar_matriz(tamanho_linha,tamanho_coluna)

matriz2 = criar_matriz(tamanho_linha,tamanho_coluna)

imprimir_matiz(multi(matriz1,matriz2))