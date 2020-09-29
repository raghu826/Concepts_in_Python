class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is Empty")

        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
        print(llist)

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

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid Index")

        if index == 0:
            self.insert_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index- 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # insert a list of values to the linked list
    def insert_values(self, data_list):
        # self.head = None
        for item in data_list:
            self.insert_end(item)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning(5)
    ll.insert_end(25)
    ll.insert_at(1, 45)
    ll.print()
    ll.insert_values(['banana', 'apple'])
    ll.print()
    ll.remove_at(3)
    ll.print()






