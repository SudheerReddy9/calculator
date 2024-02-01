nums = [12,1,18,19,21,26]

for num in nums:
    if num%5 == 0:
        print(num)
        break
else:
    print("Not Found")