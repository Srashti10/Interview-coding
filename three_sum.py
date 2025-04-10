def three_sum(arr,target):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(i+2,len(arr)):
                if arr[i]+arr[j]+arr[k] == target:
                    return f'Indicies are{i}, {j} and {k}.'
                
print(three_sum([3,57,2,4,10],15))