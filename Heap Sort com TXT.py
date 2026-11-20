import random
import time

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100):
        lista.append(random.randint(0, 1000))

    with open("numeros_aleatorios.txt", "w") as arquivo_entrada:
        for numero in lista:
            arquivo_entrada.write(f"{numero}\n")
    print("Arquivo 'numeros_aleatorios.txt' criado com sucesso!")

    lista_para_ordenar = []
    with open("numeros_aleatorios.txt", "r") as arquivo_entrada:
        for linha in arquivo_entrada:
            lista_para_ordenar.append(int(linha.strip()))

    inicio = time.time()
    lista_ordenada = heap_sort(lista_para_ordenar)
    fim = time.time()

    with open("numeros_ordenados.txt", "w") as arquivo_saida:
        for numero in lista_ordenada:
            arquivo_saida.write(f"{numero}\n")
    print("Arquivo 'numeros_ordenados.txt' criado com sucesso!")

    print(f"\nTempo de execução do Heap Sort: {fim - inicio:.5f} segundos")
    print("\nPrimeiros 10 números ordenados:", lista_ordenada[:10])
    print("Últimos 10 números ordenados:", lista_ordenada[-10:])
