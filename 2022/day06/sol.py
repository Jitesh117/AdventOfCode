with open('day06/input.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

def find_unique_four(text):
    for i in range(len(text) - 3):
        substring = text[i:i+4]
        if len(set(substring)) == 4:
            return i + 4
    
    return -1  
def find_unique_fourteen(text):
    for i in range(len(text) - 13):
        substring = text[i:i+14]
        if len(set(substring)) == 14:
            return i + 14
    
    return -1  
result = 0
for line in lines:
    print(find_unique_four(line))
    print(find_unique_fourteen(line))
