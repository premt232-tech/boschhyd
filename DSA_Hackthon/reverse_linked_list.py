'''Q6: 
Given the pointer to the head node of a linked list, change the next pointers of the nodes so 
that their order is reversed. The head pointer given may be null meaning that the initial list is 
empty. 
 
Example 
head references the list 1→2→3→NULL 
Manipulate the next pointers of each node in place and return head, now referencing the 
head of the list 3→2→1→ NULL. 
Function Description 
Complete the reverse function in the editor below. 
reverse has the following parameter: 
• SinglyLinkedListNode pointer head: a reference to the head of a list 
Returns 
• SinglyLinkedListNode pointer: a reference to the head of the reversed list
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
                
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev
       



def testrun():
    l1 = Linkedlist()
    
    
    l1.append(40)
    l1.append(50)
    l1.append(60)
    l1.append(70)

    l1.Display()
    l1.reverse()

    print("the reversed linked list :")
    l1.Display()


  
   
    
testrun()
