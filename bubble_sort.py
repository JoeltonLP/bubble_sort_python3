import sys

string = sys.argv[1]
lista_de_letra = []


for x in string:
    lista_de_letra.append(x)

tamanho_lista = len(lista_de_letra)


def ordena_letras_do_alfabeto(lista):

    lista_de_letra_ = lista

    for i in range(tamanho_lista - 1):
        for n in range(tamanho_lista - 1):
            if lista_de_letra_[n] > lista_de_letra_[n+1]:
                aux = lista_de_letra[n]
                lista_de_letra_[n] = lista_de_letra_[n+1]
                lista_de_letra_[n+1] = aux
    return lista_de_letra


print(ordena_letras_do_alfabeto(lista_de_letra))
