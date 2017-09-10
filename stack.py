def stackInit():
    stackList = []
    stackLen = 5
    for i in range(0,stackLen):
        stackList.append("")
    print(stackList)
    startPointer = 0
    endPointer = stackLen
    runStack = True
    while runStack:


stackInit()

# adds a new item to the stack, moves the end pointer forwards.
def push(endPointer, stackList):
    item = input("input item: ")
    endPointer += 1
    stackList[endPointer] = item
    return endPointer, stackList

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
    1) push item
    2) """)

# test on returning multiple values in a function
"""
stackList = [1, 2, 3, 4]
endPointer, popped = pop(0, stackList)
print(endPointer)
print(popped)
"""

