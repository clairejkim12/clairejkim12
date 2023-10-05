"""Learn names and behaviors of commonly used functions."""

__author__ = "730556575"


def all(number_list: list[int], number_given: int) -> bool:
    """To see if the all the numbers are the same as the number_given"""
    ind: int = 0
    if len(number_list) == 0:
        return False
    while ind < len(number_list):
        if number_list[ind] != number_given:
            return False
        ind = ind + 1
    return True

def max(input: list[int]) -> int: 
    """Max returining the largest in the list."""
    if len(input) == 0: 
        raise ValueError("max() arg is in empty list")
    ind: int = 1
    other: int = input[0]
    while ind < len(input):
        if input[ind] > other: 
            other = input[ind]
        ind = ind + 1
    return other

def is_equal(first_list: list[int], second_list: list[int]) -> bool: 
    """To see if every index of the both lists are the same."""
    index: int = 0 
    while index < len(first_list):
        if first_list[index] != second_list[index]:
            return False
        index = index + 1
    return True