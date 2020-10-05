class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push_front(1)
    llist.push_front(4)
    llist.push_front(1)
    llist.push_front(12)
    llist.push_front(1)
    llist.printList()
    print(llist)
