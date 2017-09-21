"""Task 6 – Queues instead of stacks
Now that you understand what a stack is (LIFO) do you think you could code a queue (FIFO)?
  Use the internet if necessary to write the code needed for a queue.  You will need to think
 about the variables (pointers) that you need to operate this different type of data type and
  how they will act differently as opposed to a stack.
"""

# Wow, there's a lot of task to complete. I will have to prioritize speed over efficiency.

""" def queue_init(queueInitLength):
    global queueList
    queueList = []
    queueLen = queueInitLength
    for i in range(0,queueLen):
        queueList.append("")
    print(queueList)
    # not sure how global variables work.. Let's just go with it I guess
    global startPointer
    startPointer = 0
    global endPointer
    endPointer = -1
    return
"""

# def push(item):

# let's do a few test

def pushtest():
    testList = ["h", "e", "l", "l", "o"]
    testList.insert(0, " ")
    testList.insert(0, "i")
    testList.insert(0, "h")
    print(testList)
pushtest()

# It works! 




