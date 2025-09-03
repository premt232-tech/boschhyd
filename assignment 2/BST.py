class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right =None
class BST:
    def __init__(self):
        self.root = None
    def insert(self ,root ,key):
        if root is None :
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left,key)
        elif key >root.key:
            root.right = self.insert(root.right,key)
        return root
    def search(self,root,key):
        if root is None or root.key == key:
            return root
        if key< root.key:
            return self.search(root.left,key)
        return self.search(root.right,key)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key ,end =" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.key ,end =" ")
            self.preorder(root.left)
            
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key ,end =" ")

def test():
    b1 =BST()
    root = None
    lt = [50,60,10,20,30,80,3,2]
    for i in lt:
        root = b1.insert(root,i)
    print(f"inorder traversal :")
    b1.inorder(root)
    print(f"\npostorder traversal :")
    b1.postorder(root)
    print(f"\npreorder traversal :")
    b1.preorder(root)
    key = 10
    print("")
    if b1.search(root,key):
        print(f"the {key} is found in Bst")
    else:
        print(f"{key} not found in Bst")
test()