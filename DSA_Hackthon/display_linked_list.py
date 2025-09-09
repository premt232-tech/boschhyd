'''Given a pointer to the head node of a linked list, print each node's data element, one per 
line. If the head pointer is null (indicating the list is empty), there is nothing to print. 
Function Description 
Complete the printLinkedList function in the editor below. 
printLinkedList has the following parameter(s): 
SinglyLinkedListNode head: a reference to the head of the list  
Print For each node, print its data value on a new line 
'''




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist :
    def __init__(self):
        self.head = None
    
    
    def append(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode


    def Display(self):
        if self.head == None:
            print("the list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data ,end = "\n")
                temp = temp.next
       



def testrun():
    l1 = Linkedlist()
    l1.Display()
    l1.append(20)
    l1.append(30)
    l1.append(40)
    l1.append(50)
    l1.Display()

  
   
    
testrun()
