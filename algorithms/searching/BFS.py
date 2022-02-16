
# implementation using simple loops

from calendar import c
import queue
from turtle import left, right


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def isALeaf(self):
        if not self.left and not self.right:
            return True
        return False

    def hasOneChild(self):
        if (self.left and not self.right) or (self.right and not self.left):
            return True
        return False

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            
            while(True):
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        break
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        break
                    current_node = current_node.right

    def traverse(self, node):
        tree = { "value": node.value}

        tree['left'] = None if not node.left else self.traverse(node.left)
        tree['right'] = None if not node.right else self.traverse(node.right)

        return tree


    def lookup(self, value):
        if not self.root:
            return None

        current_node = self.root
        
        while(current_node):
            if current_node.value == value:
                return value  
            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    def remove(self, value):
        if not self.root:
            return None

        current_node = self.root
        parent_node = None
        while(current_node):
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                # Delete that value

                # Option 1: No right child
                if current_node.right is None:
                    
                    if not parent_node:
                        self.root = current_node.left
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn-t have a left child
                elif current_node.right.left is None:
                    if not parent_node:
                        self.root = current_node.right

                    if current_node.value < parent_node.value:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right

                # Option 3: Right child that has a left child
                else:

                    # find the Right child-s left most child
                    leftmost = current_node.right.left
                    leftmostParent = current_node.right
                    
                    while(leftmost.left):
                        leftmostParent = leftmost
                        leftmost = leftmost.left



                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if (not parent_node):
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost


                return True

    def BFS(self):

        result_list = []
        queue_list = [] #priority queue -> O(n) Space complexity
                        #really width tree -> really complex
        queue_list.append(self.root)

        while(len(queue_list) != 0):
            current_node = queue_list.pop(0)    
            result_list.append(current_node.value)
            
            # insert the two children to the queque in order
            if current_node.left:
                queue_list.append(current_node.left)
            if current_node.right:
                queue_list.append(current_node.right)

            

        return result_list

    def BFS_r(self, queue_list):
        if len(queue_list) == 0:
            return []

        current_node = queue_list.pop(0)

        if current_node.left:
            queue_list.append(current_node.left)
        if current_node.right:
            queue_list.append(current_node.right)
        
        return [current_node.value] + self.BFS_r(queue_list)



myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(20)
myBST.insert(1)
myBST.insert(6)
myBST.insert(15)
myBST.insert(170)
#   9
#  4 20
#1 6 15 170

print(myBST.BFS())
print(myBST.BFS_r([myBST.root]))