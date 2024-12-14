from collections import Counter
from typing import List


# original i thought the discard_list may contain a term or substring
# so using two pointer to track whether the current char is in discard_list or not
def inject_frequency(sentence: str, discard_list: List[str]) -> str:
    char_list = []
    pointer = 0

    while pointer < len(sentence):
        idx = pointer
        while idx < len(sentence):
            curr_char = sentence[pointer:idx + 1]

            if curr_char not in discard_list:
                char_list.append(curr_char)
                break
            
            idx += 1
        
        pointer = idx + 1

    print(dict(Counter(char_list)))


# but the question says that discard_list contains character, which is not a substring
# if the char is in discard_list, just append this char without irs occur
def inject_frequency(sentence: str, discard_list: List[str]) -> str:
    # time = O(n^2)
    # space = O(n)
    if not sentence: return ""
    
    char_occur_str = ""
    for char in sentence:
        if char != " " and char not in discard_list:
            char_occur = str(sentence.count(char))
            char_occur_str += f"{char}{char_occur}"
        
        else:
            char_occur_str += char
    
    return char_occur_str


# optimized solution
def inject_frequency(sentence: str, discard_list: List[str]) -> str:
    # time = O(n)
    # space = O(n)
    if not sentence: return ""
    
    char_occur_list = []
    char_occur = Counter(sentence)
    
    for char in sentence:
        if char != " " and char not in discard_list:
            char_occur_list.append(f"{char}{char_occur[char]}")
        
        else:
            char_occur_list.append(char)
    
    return "".join(char_occur_list)