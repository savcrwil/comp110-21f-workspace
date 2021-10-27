"""Examples of functions imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 16))
    print(f"helpers.py: {__name__}")
    print("evaluated as a program")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


if __name__ == "__main__":
    # python idiom, typically call main here
    main()
# else:
    # typically not common to do anything in the case where a module is imported
    # print("evaluated as an imported module")
