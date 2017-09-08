def stackInit():
    stackList = []
    stackLen = 5
    for i in range(0,stackLen):
        stackList.append("")
    print(stackList)
    startPointer = 0
    endPointer = stackLen

stackInit()

def push(item, endPointer, stackList):
    endPointer += 1
    stackList[endPointer] = item
    return item, endPointer, stackList

def pop(endPointer, stackList):
    return stackList[endPointer]
    endPointer -= 1

