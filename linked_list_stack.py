from linked_list import *

class LinkedStack(UnorderedList):
    
    def __init__(self):
        super().__init__()

    def push(self, item):
        current = self.head
        if self.isEmpty() is not True:
            while current is not None:
                current = current.get_next()
        temp = Node(item)
        current.set_next(temp)
        temp = current

    def pop(self):
        self.remove_last()

def main():
    thisStack = LinkedStack()
    thisStack.push(42)
    thisStack.push(37)
    print(thisStack.display2())
    thisStack.pop()
    print(thisStack.display2())

if __name__ == main():
    main()
