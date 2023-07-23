from arraytoimg import *
import matplotlib.pyplot as plt


def bubble_sort(arr, path):
    n = len(arr)
    
    img_index = 0
    img_index = saveimg(arr, path, img_index)

    for i in range(n):
        # Impostiamo la variabile swapped a False per ottimizzare il processo
        swapped = False
        
        # Iteriamo da 0 a n-i-1 perché gli ultimi i elementi sono già ordinati
        for j in range(0, n-i-1):
            # Se l'elemento corrente è maggiore di quello successivo, scambiamoli
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                img_index = saveimg(arr, path, img_index)
                # Impostiamo swapped a True per indicare che ci sono stati scambi in questo passaggio
                swapped = True
        
        # Se non ci sono stati scambi in questo passaggio, allora l'array è già ordinato
        if not swapped:
            break

def insertion_sort(arr, path):
    img_index = 0
    img_index = saveimg(arr, path, img_index)

    for i in range(1, len(arr)):
        key = arr[i]  # Elemento da inserire nella parte ordinata
        j = i - 1     # Inizializza l'indice del precedente elemento nell'array ordinato

        # Sposta gli elementi maggiori di 'key' di una posizione avanti
        # finché non trova la posizione corretta per 'key'
        while j >= 0 and key < arr[j]:
            temp = arr[j + 1] 
            arr[j + 1] = arr[j]
            arr[j] = temp 
            img_index = saveimg(arr, path, img_index)

            j -= 1
            

        # Inserisce 'key' nella posizione corretta nell'array ordinato
        arr[j + 1] = key
        img_index = saveimg(arr, path, img_index)


def heapify(arr, n, radice, img_index, path):
    massimo = radice
    figlio_sinistro = 2 * radice + 1
    figlio_destro = 2 * radice + 2

    # Verifica se il figlio sinistro esiste ed è maggiore della radice
    if figlio_sinistro < n and arr[figlio_sinistro] > arr[massimo]:
        massimo = figlio_sinistro

    # Verifica se il figlio destro esiste ed è maggiore della radice
    if figlio_destro < n and arr[figlio_destro] > arr[massimo]:
        massimo = figlio_destro

    # Se l'elemento massimo non è la radice, scambia i valori
    if massimo != radice:
        arr[radice], arr[massimo] = arr[massimo], arr[radice]
        img_index = saveimg(arr, path, img_index)
        # Heapify ricorsivamente il sotto-albero interessato
        heapify(arr, n, massimo, img_index, path)
    return img_index

def heap_sort(arr, path):
    n = len(arr)

    img_index = 0
    img_index = saveimg(arr, path, img_index)
    # Costruisci un max-heap dalla lista di input
    for i in range(n // 2 - 1, -1, -1):
        img_index = heapify(arr, n, i, img_index, path)

    # Estrai gli elementi uno alla volta dal max-heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Scambia l'elemento radice (massimo) con l'ultimo elemento non ordinato
        img_index = saveimg(arr, path, img_index)
        img_index = heapify(arr, i, 0, img_index, path)  # Heapify del heap ridotto


def quicksort(arr, path):

 
    if len(arr) <= 1:
        return arr
    """
    indexes = [ 0, int(len(arr)/2), len(arr)-1 ]
    medium = 0
    for i in range(-1, len(indexes)-1):
        if (arr[indexes[i]]-arr[indexes[i-1]]) * (arr[indexes[i]]-arr[indexes[i+1]]) <= 0:
            medium = indexes[i]

    pivot = arr[medium]
    """
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left, path) + equal + quicksort(right, path)

def quicksort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort2(left) + equal + quicksort2(right)


def saveimg(array, path, i, red=None):
    plt.imsave((path+ str(i) + ".png"), getimg(array, red))
    print(i)
    return i+1


# Esempio di utilizzo
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array non ordinato:", arr)
    quicksort2(arr)
    print("Array ordinato:", arr)