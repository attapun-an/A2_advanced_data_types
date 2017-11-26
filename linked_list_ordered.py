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

        if self.isEmpty() is True:
            temp.set_next(None)
            self.head = temp


        else:
            current = current.get_next()
            # loop through while the next item is not None AND the position has not been found
            while current is not None:
                if current.get_data() > item:
                    temp.set_next(current)
                    prev.set_next(temp)
                    return
                # Advice from Buta

                # when you find a problem, look at every line separately and try to figure it out
                # only have one print statement at a time, print separately

                # you have to code more, get used to recurssion in code
                # use return, stop using print all the time

                prev = current
                # print("prev: {0}".format(prev.get_data()))
                current = current.get_next()
                # print("curr: {0}".format(current.get_data()))
            temp.set_next(current)
            prev.set_next(temp)









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
    thisList.add(40)
    thisList.display2()
    thisList.add(5)
    thisList.display2()



if __name__ == '__main__':
    main()
    # remove
