"""Practice code-writing for quiz02."""

__author__ = "Kat Leedy"


def odd_and_even(nums: list[int]) -> list[int]:
    new_nums: list[int] = []
    i: int = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            new_nums.append(nums[i])
        i += 2
    return new_nums


def odd_and_even_alternate(nums: list[int]) -> list[int]:
    new_nums: list[int] = []
    even_indexes: range = range(0, len(nums), 2)
    for index in even_indexes:
        if nums[index] % 2 == 0:
            new_nums.append(nums[index])
    return new_nums


def vowels_and_threes(word: str) -> str:
    new_word: str = ""
    i: int = 0
    while i < len(word):
        if(word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u"):
            if i % 3 != 0:
                new_word += word[i]
        else:
            if i % 3 == 0:
                new_word += word[i]
        i += 1
    return new_word


def vowels_and_threes_improved(word: str) -> str:
    new_word: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    is_vowel: bool = False
    i: int = 0
    while i < len(word):
        is_vowel = False
        for vowel in vowels:
            if word[i] == vowel:
                is_vowel = True
        if i % 3 == 0 and not is_vowel:
            new_word += word[i]
        elif is_vowel and i % 3 != 0:
            new_word += word[i]
        i += 1
    return new_word




