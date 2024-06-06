with open("input.txt") as file:
    data = file.read()

lines = data.splitlines()

def find(w, instructs):

    # split instructions
    ins = []

    for i in range(len(instructs)):
        ins.append(instructs[i].split())

    ins = [x for x in ins if x!=[]]

    # sort instructions
    sorted_ins = []
    defined = set()

    while w not in defined:

        check = ins[0][-1]

        if len(ins[0])==3 and ins[0][0].isdigit():
            sorted_ins.insert(0,ins[0])
            defined.add(check)
            ins.pop(0)
            continue
        
        inputs = [x for x in ins[0][:-2] if x.islower()]

        if set(inputs).issubset(defined):
            sorted_ins.append(ins[0])
            ins.pop(0)
            defined.add(check)
        else:
            ins.append(ins[0])
            ins.pop(0)
    
    # following instructions to assign value
    wires = {}
    while w not in wires:

        inst = sorted_ins.pop(0)

        if 'AND' in inst:
            if inst[0].isdigit():
                wires[inst[-1]] = int(inst[0]) & wires[inst[2]]
            elif inst[2].isdigit():
                wires[inst[-1]] = wires[inst[0]] & int(inst[2]) 
            else:
                wires[inst[-1]] = wires[inst[0]] & wires[inst[2]]
        elif 'OR' in inst:
            if inst[0].isdigit():
                wires[inst[-1]] = int(inst[0]) | wires[inst[2]]
            elif inst[2].isdigit():
                wires[inst[-1]] = wires[inst[0]]| int(inst[2])
            else:
                wires[inst[-1]] = wires[inst[0]] | wires[inst[2]]
        elif 'RSHIFT' in inst:
            wires[inst[-1]] = wires[inst[0]] >> int(inst[2])
        elif 'LSHIFT' in inst:
            wires[inst[-1]] = wires[inst[0]] << int(inst[2])
        elif 'NOT' in inst:
            wires[inst[-1]] = ~wires[inst[1]]   
        elif inst[0] in wires:
            wires[inst[-1]] = wires[inst[0]]
        else:
            wires[inst[-1]] = int(inst[0])

    # return value 
    return wires[w]

print(find('a', lines))