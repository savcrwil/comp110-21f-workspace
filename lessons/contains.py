"""Example of a function that processes a list."""

# define a function named contains
# we can give two arguments: a needle value we're searching for in a haystack list
# return true if needle is found in haystack, false otherwise
# loop through each index in list
# test if item stored at index is equal to needle
# return true if so
# return false after testing each item


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False

# Python idion for starting the main function


if __name__ == "__main__":
    main()