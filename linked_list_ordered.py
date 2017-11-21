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
        next = current
        if self.isEmpty() is not True:
            while next is not None:
                next = current.get_next()
                if next.get_data() <= item:
                    temp = Node()
                    temp.set_next(item)
                    current.set_next(next)
                current = next
            temp = Node()
            temp.set_next(item)
            current.set_next(next)
        else:
            temp = Node(item)
            temp.set_next(None)
            current = self.head


def main():
    thisList = OrderedList()
    thisList.add(23)

if __name__ == '__main__':
    main()
    # remove
