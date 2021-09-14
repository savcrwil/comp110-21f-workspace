"""Drawing forests in a loop."""

__author__ = "730393320"

TREE: str = "\U0001F332"
i: int = int(input("Depth: "))
tree_string: str = ""

while i > 1:
    tree_string = tree_string + TREE
    print(tree_string)
    i = i - 1
print(tree_string + TREE)
