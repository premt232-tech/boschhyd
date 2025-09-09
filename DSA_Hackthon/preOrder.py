'''
Complete the PreOrder function, which has 1 parameter: a pointer to the root of a binary 
tree. It must print the values in the tree's preorder traversal as a single line of space-
separated values
'''

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

    def preOrder(self,root):
        if root:
            print(root.key ,end =" ")
            self.preOrder(root.left)
            
            self.preOrder(root.right)
   

def testrun():
    t1 =Tree()
    root = None
    lt = [30,40,50,2,1]
    for i in lt:
        root = t1.add(root,i)
    print(f"\npreOrder traversal :")
    t1.preOrder(root)
   
testrun()