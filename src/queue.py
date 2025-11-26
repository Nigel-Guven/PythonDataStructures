#FIFO

from node import Node


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None

        temp_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:          
            self.first = self.first.next
            temp_node.next = None 
        self.length -= 1
        return temp_node

myQueue = Queue("Ireland")

myQueue.enqueue("France")
myQueue.enqueue("England")
myQueue.enqueue("Wales")
myQueue.enqueue("Scotland")

myQueue.print_queue()

myQueue.dequeue()
print()
myQueue.print_queue()