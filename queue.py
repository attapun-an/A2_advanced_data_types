"""Task 6 – Queues instead of stacks
Now that you understand what a stack is (LIFO) do you think you could code a queue (FIFO)?
  Use the internet if necessary to write the code needed for a queue.  You will need to think
 about the variables (pointers) that you need to operate this different type of data type and
  how they will act differently as opposed to a stack.
"""

# Wow, there's a lot of task to complete. I will have to prioritize speed over efficiency.

def queue_init(queueInitLength):
    global queueList
    queueList = []
    # the initial length is actually not important thanks to python's flexible list. but let's anyways
    queueLen = queueInitLength
    for i in range(0,queueLen):
        queueList.append("")
    print(queueList)
    # not sure how global variables work.. Let's just go with it I guess
    global startPointer
    startPointer = 0
    global endPointer
    endPointer = -1


def push(item):
    queueList.insert(startPointer, item)
    global endPointer
    endPointer += 1

def pop(List):
    global endPointer
    popped = List[endPointer]
    endPointer -= 1
    return popped

# let's do a few test

def pushtest():
    testList = ["h", "e", "l", "l", "o"]
    testList.insert(0, " ")
    testList.insert(0, "i")
    testList.insert(0, "h")
    print(testList)
# pushtest()

# It works!

def queueProgram():
    runQueue = True
    while runQueue:
        queue_init(0)
        QueMenu = True
        while QueMenu:
            print(queueList)
            command = input("""
            0 = exit
            1 = push
            2 = pop
            """)
            # Exit
            if command == "0":
                QueMenu = False
                runQueue = False
            # push
            elif command == "1":
                itemtopush = input(">")
                push(itemtopush)
            elif command == "2":
                if endPointer > startPointer:
                    popped=pop(queueList)
                    print(popped)
                else:
                    print("no items to pop")

# queueProgram()

class custom_Queue:
    def __init__(self, startPointer, endPointer):
        self.__startPointer = startPointer
        self.__endPointer = endPointer
        self.__array = []

    def pop(self):
        index = self.__endPointer
        popped = self.__array[index]
        self.__endPointer -= 1
        return popped

    def push(self, item):

        self.__endPointer += 1


thisQueue = custom_Queue(0, -1)
thisQueue.push("hi")
thisQueue.pop()





