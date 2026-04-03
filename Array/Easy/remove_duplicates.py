numbers = [1,2,2,2,3,4,4,5]
dupl = []
def duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(numbers)):
            if arr[i] == arr[j]:
                if arr[i] not in dupl:
                   dupl.append(arr[i])
    return dupl

print(duplicates(numbers))
