def square_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [1,2,3,4,5,6,7]
print(square_number(numbers))
