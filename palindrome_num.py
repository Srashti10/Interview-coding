# num = int(input('Enter the number: '))
# temp = str(num)
# if temp == temp[::-1]:
#     print('Number is palindrome.')
# else:
#     print('Number is not palindrome.')











# num = int(input("Enter a number: \n"))
# temp = str(num)
# if temp == temp[::-1]:
#     print("Number is Palindrome.")
# else:
#     print("Number is not Palindrome.")






def palindrome(num):
    temp = str(num)
    if temp == temp[::-1]:
        return "Number is Palindrome."
    else:
        return "Number is not Palindrome."
    
print(palindrome(23))
