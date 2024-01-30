letter = input("Enter a number: ")
num = ord(letter)
num = num + 1
print(chr(num))
cost = float(input("Enter the total cost: "))
revenue = float(input("Enter the total revenue: "))
if cost == revenue:
    result = 'Break Even'
else:
    if cost < revenue:
        profit = revenue - cost
        result = "Profit is $ " + str(profit)
    else: 
        loss = cost - revenue
        result = "Loss is $ " + str(loss)

print(result)