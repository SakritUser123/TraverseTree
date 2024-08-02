class binaryTree:
    def __init__(self,nodedata,left = None , right = None):
        self.nodedata = nodedata
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.nodedata)
        
tree = binaryTree("root")
BranchA = binaryTree("Branch A")
BranchB= binaryTree("Branch B")
tree.left = BranchA 
tree.right = BranchB
LeafC = binaryTree("LeafC")
LeafD = binaryTree("LeafD")
LeafE = binaryTree("LeafE")
LeafF = binaryTree("LeafF")
Leaf1 = binaryTree("Leaf1")
Leaf2 = binaryTree("Leaf2")
Leaf3 = binaryTree("Leaf3")
Leaf4 = binaryTree("Leaf4")
BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF
LeafC.left = Leaf1
LeafC.right = Leaf2
LeafD.left = Leaf3
LeafD.right = Leaf4

def traverse(tree):
    if tree != None:
        print(tree.nodedata)
        traverse(tree.left)
        traverse(tree.right)
    
traverse(tree)
