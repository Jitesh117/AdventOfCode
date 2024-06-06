import string

alphabet = list(string.ascii_lowercase)
alphabet.remove('i')
alphabet.remove('o')
alphabet.remove('l')

mapping = {}
reverting = {}

for i in range(len(alphabet)):
    mapping[alphabet[i]] = i
    reverting[i] = alphabet[i]

def increment(pw):
    pw[-1] = pw[-1]+1

    for i in range(len(pw)):
        if pw[i] >22:
            pw[i] = 0
            pw[i-1] = pw[i-1]+1
    return pw

def update(input):

    pw = [mapping[c] for c in input]

    test_consecutive, test_pairs = False, False 

    while test_consecutive==False or test_pairs==False:
        test_consecutive, test_pairs = False, False
        pair_count, unique_pair = 0, [] 

        pw = increment(pw)

        for i in range(len(pw)-2):
            if pw[i]+1==pw[i+1] and pw[i]+2==pw[i+2]:
                test_consecutive = True

        for i in range(len(pw)-1):
            if pw[i]==pw[i+1] and pw[i] not in unique_pair:
                pair_count += 1
                unique_pair.append(pw[i])
        if pair_count >=2:
            test_pairs = True

    new_password = ""

    for p in pw:
        new_password += reverting[p]

    return new_password


input = "cqjxjnds"
next_password = update(input)
print(next_password)
next_password = update(next_password)
print(next_password)