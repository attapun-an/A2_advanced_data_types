def stackInit():
    stackList = []
    stackLen = 20
    for i in range(0,stackLen):
        stackList.append("")
    print(stackList)
    startPointer = 0
    # endPointer = stackLen
    endPointer = -1
    runStack = True
    displayinstructions()
    while runStack:
        command = input(">")
        if command == "0":
            runStack = False
            "stack stopping"
        elif command == "1":
            print(stackList[0:endPointer+1])
        elif command == "2":
            # not sure if these things are global but I'm playing it safe (should've tested it out first)
            endPointer, stackList = push(endPointer, stackList)
        elif command == "3":
            EmptyError = checkStackEmpty(endPointer, startPointer)
            if EmptyError == True:
                print("The stack is empty and no item can be popped")
            else:
                endPointer, popped = pop(endPointer, stackList)
                print(popped)
        elif command == "4":


        elif command == "h":
            displayinstructions()


# adds a new item to the stack, moves the end pointer forwards.
def push(endPointer, stackList):
    if endPointer < len(stackList):
        item = input("input item: ")
        endPointer += 1
        stackList[endPointer] = item
        return endPointer, stackList
    else:
        print("out of range")

def splitString(thisString):
    listedString = thisString.list()
    print(listedString)


# we need a check to see if it has gone over the stack size

# increments the endPointer back 1 space and returns it's new position and the popped value
def pop(endPointer, stackList):
    popped = stackList[endPointer]
    endPointer -= 1
    return endPointer, popped

# checks if the end pointer has gone below 0 (the first slot in the stack) - meaning there's nothing to pop
def checkStackEmpty(endPointer, startPointer):
    if endPointer < startPointer:
        return True
    else:
        return False

def displayinstructions():
    print("""stack Instructions:
    0 exit
    1 preview stack
    2 push item
    3 pop
    4 reverse string
    h help (previews instructions) """)

# test on returning multiple values in a function
"""
stackList = [1, 2, 3, 4]
endPointer, popped = pop(0, stackList)
print(endPointer)
print(popped)
"""


stackInit()
