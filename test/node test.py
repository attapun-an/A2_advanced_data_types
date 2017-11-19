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

    def get_next(self) -> object:
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.next = next_node



def main():
    node1 = Node(23)
    # node1.set_data(2)
    print("node 1 data: {0}".format(node1.get_data()))

    node2 = Node(52)
    # node2.set_data(3)

    node3 = Node(89)
    print("node 3 data: {0}".format(node3.get_next()))

    current = node1
    print("current data {0}".format(current.get_data()))

    node1.set_next(node2)
    print(node1.get_next())

    # count nodes


main()





