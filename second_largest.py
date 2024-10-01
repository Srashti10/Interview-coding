arr = [12, 35, 1, 10, 34, 1]
# arr.sort()
# print(arr[len(arr)-2])
# arr =[10,10]
new_arr = list(set(arr))
new_arr.sort()
n = len(new_arr)
if new_arr[n-1] != new_arr[n-2]:
    print(new_arr[n-2])
else:
    print(-1)
