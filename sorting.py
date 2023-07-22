from arraytoimg import *
import matplotlib.pyplot as plt

def saveimg(array, path, i, conf=None):
    plt.imsave((path+ str(i) + ".png"), getimg(array))
    print(i)
    return i+1

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
            img_index = saveimg(arr, path, img_index)
            arr[j + 1] = arr[j]
            j -= 1

        # Inserisce 'key' nella posizione corretta nell'array ordinato
        img_index = saveimg(arr, path, img_index)
        arr[j + 1] = key



# Esempio di utilizzo
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array non ordinato:", arr)
    insertion_sort(arr, "exports/")
    print("Array ordinato:", arr)