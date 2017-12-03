
thisArray = [0]

def t1():
    global thisArray
    thisArray.append(1)

def t2():
    global thisArray
    thisArray.append(2)
    thisArray.append(3)

t1()
t2()

print(thisArray)
