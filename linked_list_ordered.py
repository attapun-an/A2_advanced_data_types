from LL_node import *


class OrderedList():
    def __init__(self):
        self.head = None

    # isEmpty
    def isEmpty(self):
        return self.head is None

    """Mr. M: Ca."we know if it's empty, head == None, and if we reach the
    end, we get None .Loop through it until we hit None, then add it" """
    # add
    def add(self, item):

        # set up variables

        current = self.head
        # keeps track of previous item
        prev = current
        temp = Node(item)
        found = False

        if self.isEmpty() is True:
            self.head = temp
            temp.set_next(None)

        else:
            current = current.get_next()
            # loop through while the next item is not None AND the position has not been found
            while current is not None and found is False:
                if current.get_data() < item:
                    print("checked")
                    # break the loop
                    found = True

                prev = current
                print("prev: {0}".format(prev.get_data()))
                current = current.get_next()
                print("curr: {0}".format(current.get_data()))
                print("incrimented")

            prev.set_next(temp)
            temp.set_next(current)






    def display2(self):
        current = self.head
        line = ""
        while current is not None:
            line = line + (str(current.get_data())) + " "
            current = current.get_next()
        print (line)

def main():
    thisList = OrderedList()
    thisList.add(1)
    thisList.display2()
    thisList.add(2)
    thisList.display2()
    thisList.add(3)
    thisList.display2()
    thisList.add(4)
    thisList.display2()
    thisList.add(5)
    thisList.display2()



if __name__ == '__main__':
    main()
    # remove
