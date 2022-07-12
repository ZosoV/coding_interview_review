

import queue

import queue

def level_traversal(root):

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        for i in range(q.size()):
            node = q.get()

            # TODO: something to gather in the level

            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)
        
            
