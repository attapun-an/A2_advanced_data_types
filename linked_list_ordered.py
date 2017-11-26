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

    # search
    def search(self, item):
        current = self.head
        # if the list is not empty
        if self.isEmpty() is not True:
            while current is not None:
                cur_item = current.get_data()
                if cur_item == item:
                    return {"status": "Found", "item": item}
                    # Mr. M -- return True -> can be used as a check for remove(item)
                else:
                    current = current.get_next()

            return{"status": "Not Found", "item": item}
        else:
            return{"status": "List is empty", "item": item}

    def remove_first(self):
        if self.isEmpty() is False:
            current = self.head
            self.head = current.get_next()

    def remove_last(self):
        if self.isEmpty() is False:
            current = self.head
            previous = None
            # cheat method
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            previous.set_next(None)

    def remove(self, item):
        print("attemping to remove {0}".format(item))
        # Mr. M -- This should also have a check
        current = self.head
        previous = None
        # found to print result for user (not part of looping mechanism
        found = False
        while current != None:
            if current.get_data() == item:
                previous.set_next(current.get_next())
                found = True
                break
            else:
                previous = current
                current = current.get_next()

        return found

    def disp_rem_status(self, boolean):
        if boolean == True:
            print("Item removed")
        else:
            print("Item not found")










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

    print(thisList.search(2))
    print(thisList.search(40))
    print(thisList.search(29))

    thisList.display2()
    print("""
    
    remove first""")

    thisList.remove_first()
    thisList.display2()
    print("""
    remove last""")
    thisList.remove_last()
    thisList.display2()

    remstatus = thisList.remove(3)
    thisList.disp_rem_status(remstatus)
    remstatus = thisList.remove(5)
    thisList.disp_rem_status(remstatus)
    thisList.add(40)
    thisList.display2()

    remstatus = thisList.remove(10)
    thisList.disp_rem_status(remstatus)
    





if __name__ == '__main__':
    main()
    # remove
