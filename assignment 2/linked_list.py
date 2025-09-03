class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlt :
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def append(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        
    def delete(self, value):
        if self.head is None:
            print("The list is empty")
            return

    
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    print("Value not found in the list")

    def Display(self):
        if self.head == None:
            print("the list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data ,end = " ")
                temp = temp.next
        print(" ")



def test():
    lt1 = Linkedlt()
    lt1.prepend(1)
    lt1.prepend(5)
    lt1.Display()
    lt1.append(20)
    lt1.append(30)
    lt1.Display()
    lt1.delete(5)
    lt1.Display()
    lt1.delete(20)
    lt1.Display()
test()
