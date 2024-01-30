# total = 0
# num = int(input("Enter an Even Number, (-1 to quit):"))
# while  num != -1:
#     if num % 2 == 1:
#         print("Error, only even number please")
#         num = int(input("Enter  an even number, (-1 to quit): "))
#         continue
#     total = total + num
#     num = int(input("enter an even number, (-1 to quit):")) 
# print("The sum of even numbers you entered is:" , total)
# months 
# months = ("January", "February", "March")
# for month in months :
#     if 'A' in month.upper():
#         print(month)


# reverse word
word = input('Enter a word: ')
reversedWord = ''
for ch in word:
    reversedWord = ch + reversedWord
print("the reversed word is " + reversedWord + '.')