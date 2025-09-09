'''Complete the getHeight or height function . It must return the height of a binary tree as an 
integer. getHeight or height has the following parameter(s): 
• root: a reference to the root of a binary tree'''

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right =None
class Tree:
    def __init__(self):
        self.root = None
    def add(self ,root ,key):
        if root is None :
            return Node(key)
        elif key < root.key:
            root.left = self.add(root.left,key)
        elif key >root.key:
            root.right = self.add(root.right,key)
        return root
    def height(self,root):
        if not root:
            return -1
        return max(self.height(root.left),self.height(root.right))+1

   
   

def testrun():
    t1 =Tree()
    root = None
    lt = [5 ,20,30,1,2]
    for i in lt:
        root = t1.add(root,i)
    result = t1.height(root)
    print(f"the height of root :{result}")
    
   
testrun()