"""Quiz 2 practice writing functions."""


def odd_and_even(a: list[int]) -> list[int]:
    b: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 1 and i % 2 == 0:
            b.append(a[i])
        i += 1
    return b


def vowels_and_threes(string: str) -> str:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    new_string: str = ""
    is_vowel: bool = False
    i: int = 0
    j: int = 0
    while i < len(string):
        is_vowel = False
        j = 0
        while j < len(vowels):
            if vowels[j] == string[i]:
                is_vowel = True
            j += 1
        if i % 3 == 0 and is_vowel:
            new_string += ""
        elif i % 3 == 0:
            new_string += string[i]
        elif is_vowel:
            new_string += string[i]
        i += 1
    return new_string