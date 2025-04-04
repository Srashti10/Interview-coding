# num = int(input('Enter the number'))
# sum = int((num * (num+1))/2)
# print(f'sum of {num} natural numbers is', sum)

def natural_num_sum(num):
    sum = (num*(num+1))/2
    return sum
print(int(natural_num_sum(10)))