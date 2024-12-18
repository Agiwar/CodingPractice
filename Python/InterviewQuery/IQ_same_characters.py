"""
Given a list of strings, 
write a Python program to check whether each string has all the same characters or not. 
What is the complexity of this program?

Example:

Input:
string_list = ['bbbbb', 'abc', 'aaaaaaaab']

Output: False

string bbbbb has all the same characters
string abc does not have all the same characters
string aaaaaaaab does not have all the same characters
"""

from typing import List


def same_characters(input_list: List[str]) -> bool:
    """
    n: number of n strings in input_list
    m: each string has length of m

    time = O(n * m)
    space = O(m) creating set object 
    """
    return all(len(set(string)) == 1 for string in input_list)


def same_characters(input_list: List[str]) -> bool:
    """
    n: number of n strings in input_list
    m: each string has length of m

    time = O(n * m)
    space = O(1) without creating set object 
    """
    return all(string[0] * len(string) == string for string in input_list)