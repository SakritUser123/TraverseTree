class binaryTree:
    def __init__(self, nodedata, left=None, right=None):
        self.nodedata = nodedata
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.nodedata)
        
# Create the root node
tree = binaryTree("root")

# Create branches and assign them to the root node
BranchA = binaryTree("BranchA : 0-10")
BranchB = binaryTree("BranchB: 10-20")
tree.left = BranchA
tree.right = BranchB

# Create leaves and assign them to the branches
LeafC = binaryTree("BranchA Left:0-5")
LeafD = binaryTree("BranchA right:5-10")
LeafE = binaryTree("BranchB left:10-15")
LeafF = binaryTree("BranchB right:15-20")
BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF


# Traverse the tree
def traverse(tree):
    if tree != None:
        print(tree.nodedata)
        traverse(tree.left)
        traverse(tree.right)
    
traverse(tree)
