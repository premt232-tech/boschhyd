 
class Queue:
    def __init__(self):
        self.queue= []
    def enqueue(self,value):
        self.queue.append(value)
        print(f"the {value} is add in queue ")
    def isempty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if self.isempty():
            print("queue is empty")
        else:
            p= self.queue.pop(0)
            print(f"the value is poped from the stack {p}")
    def peek(self):
        if self.isempty():
            print("queue is empty")
        else:
            print(f"the first  element in queue {self.queue[0]}")
    def size(self):
        print(f"queue size : {len(self.queue)}")
    def display(self):
        print(self.queue)

def test():
    q1 = Queue()
    q1.enqueue(5)
    q1.enqueue(55)
    q1.enqueue(555)
    q1.display()
    q1.size()
    q1.dequeue()
    q1.display()
    q1.peek()
    q1.dequeue()
    q1.peek()

test()

