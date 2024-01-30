def square_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [i for i in range(1, 10)]
print(square_number(numbers))
