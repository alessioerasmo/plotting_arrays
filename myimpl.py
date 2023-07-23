def quicksort(arr):
    do_quicksort(arr, 0, len(arr)-1)

def do_quicksort(arr, start, end):

    if end-start <= 1:
        return arr

    print("\nlunghezza array: ",end+1)

    indexes= [start, int((start+end)/2), end]
    print("indici: ",indexes)
    print("valori: ", [ arr[x] for x in indexes ] )
    
    medium = start
    for i in range(-1, len(indexes)-1):
        if (arr[indexes[i]]-arr[indexes[i-1]]) * (arr[indexes[i]]-arr[indexes[i+1]]) <= 0:
            medium = indexes[i]

    pivot = arr[medium]
    print("pivot: ", pivot)
    print("indice pivot: ", medium,"\n")
    

    # metto il pivot all'inizio
    arr[start], arr[medium] = arr[medium],arr[start]  


    next_inf = start + 1
    next_sup = end 

    print("\nho messo il pivot in posizione: ", start)
    print("devo iterare tra gli indici: ", start+1, " e ", end,"\n")
"""
    for i in range(start +1 , end):
        if (arr[i] < arr[start]):
            arr[next_inf], arr[i] = arr[i], arr[next_inf]
            next_inf+=1
        else:
            arr[next_sup], arr[i] = arr[i], arr[next_sup]
            next_sup-=1
    
    arr[next_inf-1], arr[start] = arr[start], arr[next_inf-1]
"""

    #print(arr[:next_inf-1])
    #print(arr[next_sup+1:])
    #print("metà destra: ",arr[start:next_inf-1])
    #print("metà sinistra: ",arr[next_sup+1:end+1],"\n")
    #do_quicksort(arr, start, next_inf-1)        
    #do_quicksort(arr, next_sup+1, end)

    # print(arr[medium])


# Esempio di utilizzo
if __name__ == "__main__":
    arr = [64, 34, 25, 70, 0,66, 88, 95, 2, 32, 55, 6654, 66, 11, 90]
    print("Array non ordinato:", arr)
    quicksort(arr)
    print("Array ordinato:", arr)