""""
Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares.
"""
import calendar


def pares():
    lista = list(
        range(1, 32)
    )
    qtdpares = 0
    print("conteudo da lista\n", lista)
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            qtdpares += 1
    print(qtdpares)


def paresWhile():
    lista = list(
        range(1, 32)
    )
    qtdpares = 0
    print("conteudo da lista com  while \n", lista)
    i = 0
    tamlista = len(lista)
    while i < tamlista:
        if lista[i] % 2 == 0:
            qtdpares += 1
        i += 1
    print(qtdpares)


"""
Faça um programa que peça para o usuário digitar uma palavra e imprima
cada letra em uma linha.
"""


def soletre():
    while True:
        palavra = input("digite uma palavra:")
        if len(palavra) > 0:
            for i in range(len(palavra)):
                print(palavra[i])
            break
        else:
            print("digite uma palavra valida ")


def soma_matriz():
    """
    Faça um programa que peça para o usuário digitar uma palavra e imprima
    cada letra em uma linha.
    """
    mtz = []
    mtz1 = [6, 7, 8, 9, 10]
    mtz2 = [12, 43, 5, 1, 20]
    print(mtz1)
    print(mtz2)
    while True:
        if len(mtz1) == len(mtz2):
            for i in range(len(mtz1)):
                mtz.append(mtz1[i]+mtz2[i])
            print("a soma da matr", mtz)
            break
        else:
            print("as Matrizes nao sao do mesmo tamanho")



"""
Crie um dicionário cujas chaves são os meses do ano e os valores são a
duração (em dias) de cada mês.
Exemplo:
Janeiro - 31
Fevereiro - 28
Março - 31
Etc...
"""
def mesesAno():

    listMesano = {}
    listMesano ={
        "janeiro":  31,
        "fevereiro": 28,
        "março":	31,
        "abril":	30,
        "maio": 	31,
        "junho":	30,
        "julho":	31,
        "agosto":	31,
        "setembro":	30,
        "outubro":	31,
        "novembro":	30,
        "dezembro":	31,
    }
    print("lista:", listMesano ,'\n')
    print("exerc 5 - listado individual")
    for mes  in listMesano.keys():
        print(f'Mês {mes} -> {listMesano[mes] }' )

print("exercicio 1:  ")
pares()
print("exercicio 1 com while :  ")
paresWhile()
print("exercicio 2: soletre ")
soletre()
print("exercicio 3: soma matriz")
soma_matriz()
print("exercicio 4 e 5 :  lista mes ano")
mesesAno()

