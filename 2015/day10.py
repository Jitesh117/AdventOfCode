input = "1113222113"
def repeats(input):
    separated = [i for i in input]
    repeats = [input[0]]

    for i in range(1,len(separated)):
        if separated[i]==separated[i-1]:
            repeats[-1] = repeats[-1]+separated[i]
        else:
            repeats.append(separated[i])
    return repeats

for i in range(40):
    groups = repeats(input)
    input = ""
    for group in groups:
        input += str(len(group)) + str(group[0])

print(len(input))

for i in range(10):
    groups = repeats(input)
    input = ""
    for group in groups:
        input += str(len(group)) + str(group[0])

print(len(input))