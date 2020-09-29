# Creating a stack Data Structure

from collections import deque


class Stack:
    def __init__(self,):        # create a deque for stacking
        self.box = deque()

    def push(self, val):        # to add values to stack
        self.box.append(val)

    def pop(self):              # to delete the last value in the stack
        return self.box.pop()

    def peek(self):             # to access the last value
        return self.box[-1]

    def is_empty(self):         # to check stack is empty or not
        if len(self.box) == 0:
            return True

    def length(self):
        return len(self.box)

# to reverse the string using the functions push and pop
    def reverse_string(self, data):
        for i in data:
            self.push(i)

        rstr = ''
        while self.length() != 0:
            rstr += self.pop()

        print("the reverse order of the given string is", rstr)


if __name__ == "__main__":
    s = Stack()
    s.reverse_string("hi everyone")
    s.reverse_string("my name is raghu")