import hashlib

with open('input.txt', 'r') as file:
    input = file.read()
number = 0

while True:
    key = input + str(number)
    if hashlib.md5(key.encode()).hexdigest().startswith('000000'):
        break
    number += 1

print(number)