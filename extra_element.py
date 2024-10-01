arr1 = [2,4,6,8,9,10,12]
arr2 = [2,4,6,8,10,12]
n1 = len(arr1)
n2 = len(arr2)
for i in (0,n1-1):
    for j in (0,n2-1):
        if arr1[i] != arr2[j]:
            print(i)
