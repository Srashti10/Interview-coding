def digit_sum(num):
    sum = 0
    for digits in str(num):
        sum = sum + int(digits)
    return sum

num = int(input('Enter the number: '))
print(digit_sum(num))





# num = int(input("Enter a number:"))
# sum = 0 
# for i in str(num):
#     sum += int(i)
# print(sum)