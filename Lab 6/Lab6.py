#Syed Yasoob Ali
#500953533
#Lab 6

#Recieved help from friend at Laurier University


#node of BST tree
class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#Insert node into BST tree
def insert_node(root, data):

    #Creates a root if there is none
    if root is None:
        return BSTNode(data)

    #If the data is already in the tree, return the node
    elif root.data == data:
        return root

    #If the data is more than the current value, create a node
    elif root.data < data:
        root.right = insert_node(root.right, data)

    #same as above but for left side
    else:
        root.left = insert_node(root.left, data)

    #Returns the root of the tree after it inserts the node
    return root


#Finds the minimum node 
def min_node(node):

    if node is None:
        return node

    #Keeps going left until it finds the minimum node
    while(node.left is not None):
        node = node.left

    #returns minimum node
    return node


#Finds the maximum node
def max_node(node):

    if node is None:
        return node

    #Keeps going right until it finds the maximum node
    while(node.right is not None):
        node = node.right

    #returns maximum node
    return node


#Deletes a node
def delete_node(root, data):

    #If root is none, return it
    if root is None:
        return root

    #If the node is on the left side
    if data < root.data:
        root.left = delete_node(root.left, data)

    #If the node is on the right side
    elif data > root.data:
        root.right = delete_node(root.right, data)

    else:
        #If you need to delete the root with 1 or 0 child. If left child not present, remove and return right child
        #If right child not present, remove and return left child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #If there are 2 childs, it will take the lowest value from right side and replace it with current
        temp = min_node(root.right)
        root.data = temp.data
        #deletes lowest value from right side
        root.right = delete_node(root.right, temp.data)

    #Returns root of tree after it deletes node    
    return root


#print the BST
def print_bst(root):
    print_height(root)
    print("InOrder: ", end = " ")
    inorder(root)


#print height of the tree
def print_height(root):
    print(f"Height: {depth(root) - 1 }, min={min_node(root).data}, max={max_node(root).data}")


#inOrder function
def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


#depth function
def depth(root):

    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))


#Print everything required for lab

if __name__ == "__main__":
    bst = BSTNode(50)
    bst = insert_node(bst, 20)
    bst = insert_node(bst, 30)
    bst = insert_node(bst, 90)
    bst = insert_node(bst, 40)
    bst = insert_node(bst, 50)
    bst = insert_node(bst, 70)
    print("Insertion: ")
    print_bst(bst)
    delete_node(bst, 70)
    print("\nDeletion of 70: ")
    print_bst(bst)
    delete_node(bst, 40)
    print("\nDeletion of 40: ")
    print_bst(bst)
    
    
