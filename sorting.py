from arraytoimg import *
import matplotlib.pyplot as plt

def saveimg(array, path, i, conf=None):
    if conf is None:
        plt.imsave((path+ str(i) + ".png"), getimg(array))
    else:
        plt.imsave((path+ str(i) + ".png"), getimg(array, conf))    
    return i+1

def bubble_sort(arr, path):
    n = len(arr)
    
    i = 0
    i = saveimg(arr, path, i)

    for i in range(n):
        # Impostiamo la variabile swapped a False per ottimizzare il processo
        swapped = False
        
        # Iteriamo da 0 a n-i-1 perché gli ultimi i elementi sono già ordinati
        for j in range(0, n-i-1):
            # Se l'elemento corrente è maggiore di quello successivo, scambiamoli
            i = saveimg(arr, path, i, conf=(j, j+1))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                i = saveimg(arr, path, i)
                # Impostiamo swapped a True per indicare che ci sono stati scambi in questo passaggio
                swapped = True
        
        # Se non ci sono stati scambi in questo passaggio, allora l'array è già ordinato
        if not swapped:
            break

# Esempio di utilizzo
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array non ordinato:", arr)
    bubble_sort(arr, "exports/")
    print("Array ordinato:", arr)