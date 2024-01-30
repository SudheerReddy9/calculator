import string
import random
alphabets = str(string.ascii_letters)
numbers = "0123456789"
symbols = "[]_!@#$%^&*()"
all = alphabets + numbers + symbols
length = 16

password = "".join(random.sample(all,length))
print("Your Password is: \n", password)

