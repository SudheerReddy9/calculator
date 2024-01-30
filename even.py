
def even_or_odd(num):
    #num = int(input("Please Enter the number: "))
    if(num & 1) == 0:
        print(num & 1)
        return f"{num} is even"
    else:
        print(num & 1)
        return f"{num} is odd"
print(even_or_odd(3))