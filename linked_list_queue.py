from linked_list import *

# first one in, first one out
class LinkedQueue(UnorderedList):
    
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.add(item)

    def pop(self):
        self.remove_last()

def main():
    thisQueue = LinkedQueue()
    thisQueue.push(42)
    thisQueue.push(37)
    thisQueue.push(27)
    print(thisQueue.display2())
    thisQueue.pop()
    print(thisQueue.display2())

if __name__ == main():
    main()
