class Node:
    def __init__(self, value, color='RED', parent=None, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color='BLACK')  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value, left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            parent = node.parent
            grandparent = parent.parent

            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.color == 'RED':
                    parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    grandparent.color = 'RED'
                    node = grandparent
                else:
                    if node == parent.right:
                        node = parent
                        self.left_rotate(node)
                    parent.color = 'BLACK'
                    grandparent.color = 'RED'
                    self.right_rotate(grandparent)
            else:
                uncle = grandparent.left
                if uncle.color == 'RED':
                    parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    grandparent.color = 'RED'
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        self.right_rotate(node)
                    parent.color = 'BLACK'
                    grandparent.color = 'RED'
                    self.left_rotate(grandparent)

        self.root.color = 'BLACK'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, value):
        node = self.root
        while node != self.NIL and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if node == self.NIL:
            return  # Node not found

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 'BLACK':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def search(self, value):
        current = self.root
        while current != self.NIL and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current != self.NIL

    def get_black_height(self):
        def black_height(node):
            if node == self.NIL:
                return 1
            left_height = black_height(node.left)
            return left_height + (1 if node.color == 'BLACK' else 0)

        return black_height(self.root)

    # Function to print the tree
    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, end='')
            if last:
                print("R----", end='')  # Root node is denoted as 'R----'
                indent += "     "
            else:
                print("L----", end='')  # Left child denoted as 'L----'
                indent += "|    "

            color = "RED" if node.color == 'RED' else "BLACK"
            print(f"{node.value}({color})")

            # Recursive calls for left and right subtrees
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)


# Example usage:
rb_tree = RedBlackTree()

# Insert nodes
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.insert(15)
rb_tree.insert(25)

# Print the tree structure before deletion
print("Before deletion:")
rb_tree.print_tree(rb_tree.root)
print("Before deletion:", rb_tree.get_black_height())

# Delete a node
rb_tree.delete(20)

# Print the tree structure after deletion
print("\nAfter deletion:")
rb_tree.print_tree(rb_tree.root)
print("After deletion:", rb_tree.get_black_height())