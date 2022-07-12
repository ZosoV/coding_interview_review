

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order(node):

    if node:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):

    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)

def post_order(node):

    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)

def pre_order_no_recursive(node):
    
    stack = []
    stack.append(node)

    while(len(stack) != 0):
        
        node = stack.pop()

        if node:
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)
            


def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion
    if i < n:
        root = TreeNode(arr[i])
 
        # insert left child
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
 
        # insert right child
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
         
    return root

# arr = [7,4,3,None,None,6,19]
arr_preorder = [1, 2, 5, 3, 4, 6, 7]
arr_inorder = [4, 2, 6, 1, 3, 5, 7]
arr_postorder = [7, 3, 6, 1, 2, 4, 5]

root = insertLevelOrder(arr_preorder, 0, len(arr_preorder))
pre_order(root)
print("---")
pre_order_no_recursive(root)

print("---")
root = insertLevelOrder(arr_inorder, 0, len(arr_inorder))
in_order(root)


print("---")
root = insertLevelOrder(arr_postorder, 0, len(arr_postorder))
post_order(root)