n = 5
for i in range(0, n):
    for j in range(0, n-1):
        print(end = '')
    for j in range(0, i+1):
        print('*', end = ' ')
    print()


# def triangle(n):
# 	k = n - 1
# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1
# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print()
# n = 5
# triangle(n)
def triangle(n):
    for i in range(1, n+1):
        print(" " * (n-i) + ' *' * (i))
triangle(5) 
