import math

def read_in(input):
    with open(input) as fh:  
        return [line.strip() for line in fh]

def day1():
    modules = read_in("d1p1.txt")
    #modules = [100756]
    sum = 0
    for m in modules:
        sum += (math.floor(int(m)/3)-2)
    print(sum)
    print("part 2")
    sum = 0
    for m in modules:
        s = (math.floor(int(m)/3)-2)
        fuel = s
        while fuel > 0:
            fuel = (math.floor(fuel/3)-2)
            if fuel > 0:
                s += fuel
        sum += s
    print(sum)

def day2():
    code = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,5,19,23,1,6,23,27,1,27,
            10,31,1,31,5,35,2,10,35,39,1,9,39,43,1,43,5,47,1,47,6,51,2,51,6,55,
            1,13,55,59,2,6,59,63,1,63,5,67,2,10,67,71,1,9,71,75,1,75,13,79,1,
            10,79,83,2,83,13,87,1,87,6,91,1,5,91,95,2,95,9,99,1,5,99,103,1,103,
            6,107,2,107,13,111,1,111,10,115,2,10,115,119,1,9,119,123,1,123,9,
            127,1,13,127,131,2,10,131,135,1,135,5,139,1,2,139,143,1,143,5,0,99,
            2,0,14,0]
    k = 0
    while k < len(code):
        op = code[k]
        i1 = code[k+1]
        i2 = code[k+2]
        o  = code[k+3]
        if op == 1:
            code[o] = code[i1]+code[i2]
        elif op == 2:
            code[o] = code[i1]*code[i2]
        elif op == 99:
            break
        else:
            print(code)
            print(k)
        k += 4
    print(code[0])
    origCode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,5,19,23,1,6,23,27,1,27,
            10,31,1,31,5,35,2,10,35,39,1,9,39,43,1,43,5,47,1,47,6,51,2,51,6,55,
            1,13,55,59,2,6,59,63,1,63,5,67,2,10,67,71,1,9,71,75,1,75,13,79,1,
            10,79,83,2,83,13,87,1,87,6,91,1,5,91,95,2,95,9,99,1,5,99,103,1,103,
            6,107,2,107,13,111,1,111,10,115,2,10,115,119,1,9,119,123,1,123,9,
            127,1,13,127,131,2,10,131,135,1,135,5,139,1,2,139,143,1,143,5,0,99,
            2,0,14,0]
    print("part 2")
    I = 0
    J = 0
    for i in range(101):
        for j in range(101):
            code = origCode[:]
            code[1] = i
            code[2] = j
            k = 0
            try:
                while k < len(code):
                    op = code[k]
                    i1 = code[k+1]
                    i2 = code[k+2]
                    o  = code[k+3]
                    if op == 1:
                        code[o] = code[i1]+code[i2]
                    elif op == 2:
                        code[o] = code[i1]*code[i2]
                    elif op == 99:
                        break

                    k += 4
                if code[0] == 19690720:
                    print(i, j)
                    I = i
                    J = j
            except:
                1+1
    print(I, J)




print("Day 1")
day1()
print("Day 2")
day2()


