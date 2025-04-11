class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def InsertBST(x, T):
    if T is None:
        return TreeNode(x)
    if x < T.key:
        T.left = InsertBST(x, T.left)
    elif x > T.key:
        T.right = InsertBST(x, T.right)
    # If x == T.key, do nothing (or handle duplicates if needed)
    return T

def DeleteBST(x, T):
    if T is None:
        return None

    if x < T.key:
        T.left = DeleteBST(x, T.left)
    elif x > T.key:
        T.right = DeleteBST(x, T.right)
    else:
        # Node with only one child or no child
        if T.left is None:
            return T.right
        elif T.right is None:
            return T.left
        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        min_larger_node = T.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        T.key = min_larger_node.key  # Copy the inorder successor's value to this node
        T.right = DeleteBST(min_larger_node.key, T.right)  # Delete the inorder successor

    return T

# Example usage:
def inorder_traversal(T):
    if T:
        inorder_traversal(T.left)
        print(T.key, end=' ')
        inorder_traversal(T.right)

# Testing
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = InsertBST(val, root)

print("Inorder after insertion:")
inorder_traversal(root)

root = DeleteBST(50, root)
print("\nInorder after deleting 50:")
inorder_traversal(root)