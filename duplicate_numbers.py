numbers = [1,33,25,56,98,98,56]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            print(f"{numbers[i]} is duplicate")
#             break
            
# for i in range(len(numbers)):
#     if numbers[i] == duplicate:
#         print(numbers[i])
