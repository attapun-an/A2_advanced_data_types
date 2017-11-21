from LL_node import *

"""
Properties:
head -> Pointer to the first item in the list

Methods
isEmpty -> Returns True or False
add -> Add an item to the list
size -> Return the size of the list
search -> Find an item in the list
removeFront -> Remove first item in the list
removeLast -> Remove the last item in the list

help at
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
"""


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        # returns True if head is None. False if head is anything else.
        return self.head is None # can also be done with self.head == None

    def get_size(self):
        current = self.head
        size = 0
        if self.isEmpty() is not True:
            while current is not None:
                size += 1
                current = current.get_next()
        return size

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
        # Mr. M -- This should also have a check
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()
            if current.get_data() == item:
                previous.set_next(current.get_next())
                break

    def display_test(self):
        current = self.head
        # self.head points to the Node..
        print(current.get_data())
        current = current.get_next()
        print(current.get_data())
        current = current.get_next()
        print(current.get_data())
        current = current.get_next()

    def display2(self):
        current = self.head
        line = ""
        while current is not None:
            line = line + (str(current.get_data())) + " "
            current = current.get_next()
        print (line)



def main():
    thisList = UnorderedList()
    print("new list created")
    print("empty check {0}".format(thisList.isEmpty()))
    thisList.add(15)
    thisList.add(23)
    thisList.add(53)

    print("3 items have been added")
    print("empty check {0}".format(thisList.isEmpty()))

    # lets go through the items and see if they are connected:
    # thisList.display_test()
    # now let's loop
    thisList.display2()

    # get_size
    print("check size: {0}".format(thisList.get_size()))

    # search (normal val)
    print()
    result = thisList.search(15)
    print(result["status"])
    print(result["item"])

    # search abnormal data
    print()
    result = thisList.search(100)
    print(result["status"])
    print(result["item"])

    # works for the time being

    # add more items for removal
    thisList.add(120)
    thisList.add(150)
    print("full list")
    thisList.display2()

    print("remove first")
    thisList.remove_first()
    thisList.display2()

    print("remove last")
    thisList.remove_last()
    thisList.display2()

    thisList.remove_last()
    thisList.display2()

    # lets remove 53
    thisList.remove(53)
    thisList.display2()





if __name__ == main():
    main()

