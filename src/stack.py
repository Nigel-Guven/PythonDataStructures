#LIFO

from hello_world import Cookie
from node import Node


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        self.height -= 1
        return temp_node

cookie1 = Cookie('green')
cookie2 = Cookie('blue')
cookie3 = Cookie('yellow')
cookie4 = Cookie('orange')
cookie5 = Cookie('red')

myStack = Stack(cookie1)

myStack.push(cookie2)
myStack.push(cookie3)
myStack.push(cookie4)
myStack.push(cookie5)

myStack.print_stack()

myStack.pop()
print()
myStack.print_stack()

            

