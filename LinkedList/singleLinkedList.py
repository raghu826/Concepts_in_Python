class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def delete_beginning(self):
        

    def print(self):
        if self.head is None:
            print("Linked list is Empty")

        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
        print(llist)


if __name__ ==  '__main__':
    ll = LinkedList()
    ll.insert_beginning(5)
    ll.insert_end(25)
    ll.print()





