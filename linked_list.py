class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def insertafter(self, prev_node, data):
        node = Node(data)
        temp = self.head
        while temp != prev_node:
            temp = temp.next

        node.next = temp.next
        temp.next = node

        return self.head

    def linked_list_validation(self, head):
        if head:
            return True
        return False

    def middle(self):

        slow_Ptr = self.head
        fast_ptr = self.head

        while fast_ptr.next != None or fast_ptr != None:
            slow_Ptr = slow_Ptr.next
            fast_ptr = fast_ptr.next.next

        print(slow_Ptr.data)

    def remove_duplicates_sorted_ll(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

    def reverse(self):
        if not self.head:
            return
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return self.head

    def flattening(self):
        pass

    def add_one_ll(self):
        head = self.reverse()
        temp = head
        carry = 1
        while temp:
            temp.data += carry
            if temp.data % 10 == 0:
                temp.data = 0
                carry = 1
            else:
                carry = 0
            temp = temp.next
        if carry:
            llist.push_front(carry)
        print(carry)
        return self.reverse()

    def reverse_in_k(self):
        pass

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next != None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                return True
        return False

    def loop_len(self):
        pass

    def remove_loop(self):
        pass

    def nth_from_end(self):
        pass


""""
circular Linked list
"""


























if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    # llist.push_front(9)
    llist.push_front(1)
    llist.push_front(2)
    llist.push_front(3)
    llist.push_front(4)
    llist.printList()
    # llist.remove_duplicates_sorted_ll()
    # llist.reverse()
    print("---------------")
    # llist.add_one_ll()

    llist.printList()

    # print(llist)
