class Node:
    def __init__(self, init_data):
        # the data stored in the node
        self.data = init_data
        # the pointer to the next item in the list
        self.next = None
        """none is a null value. we assume that they don't
         point to anything yet (just creating nodes)
         if it doesn't point to anything - we know it's not
         in a list, or it's at the end"""

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.next = next_node


"""
def main():
    node1 = Node()
    node1.set_data(2)

    node2 = Node()
    node2.set_data(3)

    node1.set_next(node2)
    print(node1.get_next())


if __name__ == main():
    main()

"""

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
        return self.head is None
        # can also be done with self.head == None

    def get_size(self):
        current = Node(self.head)
        size = 0
        if self.isEmpty() is not True:
            while current != None:
                size += 1
                current = current.get_next()
        return size

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        # Update. this makes current into a NODE
        current = self.head
        # no idea if this will work or not
        while not self.isEmpty() or current.get_data() != item:
            # no idea if this will work either
            current = current.get_next()
        if current.get_data is not None:
            return current.get_data()
        else:
            return "item not found"

    def remove(self, item):
        current = self.head
        previous = None
        while not self.isEmpty() or current != item:
            previous = current
            current = current.get_next()
        previous.set_next(current)

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
        while current != None:
            print(current.get_data())
            current = current.get_next()





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
    thisList.display_test()
    # now let's loop
    thisList.display2()

    # print("check size: {0}".format(thisList.get_size()))



if __name__ == main():
    main()
