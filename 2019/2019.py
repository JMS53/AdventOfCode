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




day1()
