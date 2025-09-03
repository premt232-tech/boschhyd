class Stack :
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
        print(f"the {value} is pushed in stack ")
    def isempty(self):
        return len(self.stack) == 0
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            p= self.stack.pop()
            print(f"the value is poped from the stack {p}")
    def peek(self):
        if self.isempty():
            print("stack is empty")
        else:
            print(f"the top element in stack {self.stack[-1]}")
    def size(self):
        print(f"stack size : {len(self.stack)}")
    def display(self):
        print(self.stack)

def test():
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    s1.push(5)
    s1.peek()
    s1.pop()
    s1.size()
    s1.push(50)
    s1.display()
    s1.size()
test()

