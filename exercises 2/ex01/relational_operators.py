"""My own relational operators program."""

__author__ = "730393320"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
left_str: str = str(left)
right_str: str = str(right)
print(left_str + " < " + right_str + " is " + str(left < right))
print(left_str + " >= " + right_str + " is " + str(left >= right))
print(left_str + " == " + right_str + " is " + str(left == right))
print(left_str + " != " + right_str + " is " + str(left != right))
