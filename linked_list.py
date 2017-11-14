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


class LinkedList:

    
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        head = temp

    def get_size(self):
        current = self.head
        size = 0
        found = False
        while current.get_next != None or found == True:
            current = current.get_next
            size += 1
            

    # search

    # remove

def main():
    thisList = UnorderedList()
    print(thisList.get_data())

if __name__ == main():
    main()
