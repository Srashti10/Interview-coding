# arr = [1,2,3,5]
# n = 5
# sum1 = int((n*(n+1))/2)
# sum2 = 0
# for i in arr:
#     sum2 = sum2 + i
# print(sum1)
# print(sum2)
# m = sum1 - sum2
# print(m)




arr = [1,2,4,5]
n = 5
sum1 = sum(arr)
sum2 = (n*(n+1))/2
print("The missing number is",int(sum2-sum1))