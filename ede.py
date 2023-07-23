
arr = [12,1]

indexes= [0, int(len(arr)/2), len(arr)-1]
print(indexes)
print([arr[x] for x in indexes])

medium = 0
for i in range(-1, len(indexes)-1):
    if (arr[indexes[i]]-arr[indexes[i-1]]) * (arr[indexes[i]]-arr[indexes[i+1]]) <= 0:
        medium = indexes[i]


print("index: ",medium, " value: ", arr[medium])



