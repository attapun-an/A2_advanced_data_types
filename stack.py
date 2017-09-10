def stackInit():
    stackList = []
    stackLen = 5
    for i in range(0,stackLen):
        stackList.append("")
    print(stackList)
    startPointer = 0
    endPointer = stackLen

#stackInit()

def push(item, endPointer, stackList):
    endPointer += 1
    stackList[endPointer] = item
    return item, endPointer, stackList

def pop(endPointer, stackList):
    popped = stackList[endPointer]
    endPointer -= 1
    return endPointer, popped

# test on returning multiple values in a function
"""
stackList = [1, 2, 3, 4]
endPointer, popped = pop(0, stackList)
print(endPointer)
print(popped)
"""

