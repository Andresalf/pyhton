from Queue import Queue

def get_number_of_leaves(root):
    count = 0
    if root:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node.right and not node.left:
                count += 1
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
    
    return count

def get_printable_tree(root, depth=0):
    output = ""

    if root.right:
        output += get_printable_tree(root.right, depth + 1)

    output += "\n" + ("    " * depth) + str(root.data)

    if root.left:
        output += get_printable_tree(root.left, depth + 1)

    return output

def get_level_order_values(root):
    output = "{"
    if root:
        queue = Queue() 
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            output += str(node.data) + ","
            if node.left:
                queue.put(node.left)
            else:
                output += "#,"
            if node.right:
                queue.put(node.right)
            else:
                output += "#,"