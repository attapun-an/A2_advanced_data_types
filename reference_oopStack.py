"""I have no rights over this code; it wasn't coded by me - haven't gone over the copy
 right and ethics module yet - so... I hope it's okay to have it here for education purposes"""


# classes should start with capitals.
class Stack:
    """A stack of data"""

    # constructor - This runs automatically when the class is instantiated
    # self is the stack itself, that's why we always pass self to it
    def __init__(self):
        # set the initial values of the attributes
        """
         the underscore indicates they are private and can only be accessed by this class
         private means only the methods inside of this class can change it* (it can't be used outside the class)
         *Mr. Murphy has a way around that..
        """
        self._startPointer = 0
        self._endPointer = -1
        self._stackArray = ["", "", "","", "", "", "", "","", ""]

    def status(self):
        # we will return a dictionary containing the endPointer, startPointer and the stackArray
        """ usually when we use an array we need to index it pos '1', pos '2'
         at some point we may want something that can send back loads of information
         if we give it a name, it's more like a variable """
        return{"Start Pointer": self._startPointer, "End Pointer": self._endPointer, "Array Status": self._stackArray}


    def push(self, item):
        self._endPointer += 1
        self._stackArray[self._endPointer] = item
        print("You have just added {0} to the stack".format(item))

        """
        push doesn't have a _ before it but 'isEmpty' does 
        that's because the user doesn't need to interact with it - only
        the methods of the class can access it (it's private
        this is a good way of hiding code, having things go in the 
        background. So the user can't call it - since that wouldn't
        be useful to them out of order, and it may affect code
        integrity
        """

    def _isEmpty(self):
        if self._endPointer < 0:
            empty = True
        else:
            empty = False
            """empty is only a variable, and that's fine"""
        return empty

    def pop(self):
        empty = self._isEmpty()
        if empty == False:
            print("You have just popped {0} from the stack".format(self._stackArray[self._endPointer]))
            self._endPointer -= 1
        else:
            print("The stack is empty and therefore you cannot pop")

def main():
    newStack = Stack()
    print(newStack.status())
    newStack.push(4)
    print(newStack.status())
    newStack.push(5)
    print(newStack.status())
    newStack.push(6)
    print(newStack.status())
    newStack.pop()
    print(newStack.status())
    print(newStack.status()["End Pointer"])

    stack2 = Stack()
    print(newStack.status())
    stack2.push(4)
    print(newStack.status())
    newStack.pop()


main()
