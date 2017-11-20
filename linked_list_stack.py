from linked_list import *

# couldn't get node methods to work so trying to init

class NewNode(Node):

    def __init__(self):
        super().__init__(None)


# first one in, last one out
class LinkedStack(UnorderedList):
    
    def __init__(self):
        super().__init__()

    # needs to add to the end
    def push(self, item):
        self.add(item)

    def pop(self):
        self.remove_first()


def main():
    thisStack = LinkedStack()
    thisStack.push(42)
    thisStack.push(37)
    thisStack.push(22)
    print(thisStack.display2())
    thisStack.pop()
    print(thisStack.display2())

if __name__ == main():
    main()
