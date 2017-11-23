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
        current = self.head
        # keeps track of previous item
        prev = current
        found = False
        # loop through till the next item is == None AND the position has not been found
        while current.get_data(current.get_next()) is not None and found is False:
            current = current.get_next()
            
            if current.get_data < item:
                # break the loop
                found = True
            else:
                prev = current

        # generate node for item
        temp = Node(item)
        if prev == self.head:
            prev = temp
        else:
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


if __name__ == '__main__':
    main()
    # remove
