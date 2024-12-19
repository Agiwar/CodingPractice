"""
Given two strings, string1 and string2, 
write a function str_map to determine if there exists a one-to-one correspondence (bijection) 
between the characters of string1 and string2.

For the two strings, our correspondence must be between characters in the same position/index.

Example 1:

Input:
string1 = 'qwe'
string2 = 'asd'

string_map(string1, string2) == True 
# q = a, w = s, and e = d


Example 2:

Input:
string1 = 'donut'
string2 = 'fatty'

string_map(string1, string2) == False 
# cannot map two distinct characters to two equal characters


Example 3:

Input:
string1 = 'enemy'
string2 = 'enemy'

string_map(string1, string2) == True
# there exists a one-to-one correspondence between equivalent strings


Example 4:

Input:
string1 = 'enemy'
string2 = 'ymene'

string_map(string1, string2) == False
# since our correspondence must be between characters of the same index, 
# this case returns 'False' as we must map e = y AND e = e
"""


def str_map(string1: str, string2: str) -> bool:
    """
    time = O(n) 
        • for loop: O(n)
        • check membership in set: O(1), set is hash-based data structure
    space = O(n)
    """
    if not string1 or not string2 or len(string1) != len(string2):
        return False
    
    elif string1 == string2:
        return True
    
    char_seen = set()
    for char_1, char_2 in zip(string1, string2):
        if char_1 == char_2 and char_1 not in char_seen:
            continue

        if char_1 in char_seen or char_2 in char_seen:
            return False
                
        char_seen.add(char_1)
        char_seen.add(char_2)
    
    return True

# ((q, a), 
# (w, s), 
# (e, d)) -> true



# ((d, f), 
# (o, a), 
# (n, t), 
# (u, t), 
# (t, y)) -> false



# ((e, e), 
# (n, n), 
# (e, e), 
# (m, m), 
# (y, y)) -> true



# ((e, y), 
# (n, m), 
# (e, e), 
# (m, n), 
# (y, e)) -> false



def str_map(string1: str, string2: str) -> bool:
    """
    time = O(n), n is length of string
    space = O(k), k is unique character count from string
    """
    if len(string1) != len(string2):
        return False
    
    char_map1, char_map2 = {}, {}
    for char1, char2 in zip(string1, string2):
        if char1 not in char_map1 and char2 not in char_map2:
            char_map1[char1] = char2
            char_map2[char2] = char1
        
        # doesn't guarantee which char_map has no the char currently iteration
        # so using dict.get() to avoid key error
        # if one of char_map's key's value isn't equal to the current char, this means there's a 1-to-many relation
        elif char_map1.get(char1) != char2 or char_map2.get(char_map2) != char1:
            return False

    return True



def str_map(string1: str, string2: str) -> bool:
    """
    time = O(n), n is length of string
    space = O(k), k is unique character count from string
    """
    if len(string1) != len(string2):
        return False
    
    char_map1, char_map2 = {}, {}
    for char1, char2 in zip(string1, string2):
        if (char_map1.get(char1, char2) != char2 or
            char_map2.get(char2, char1) != char1
        ):
            return False
        
        char_map1[char1] = char2
        char_map2[char2] = char1
    
    return True