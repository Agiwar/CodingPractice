"""
Example 1:

Input:
string = 'banana' 
n=2

Output:
output = {'ba':1, 'an':2, 'na':2} 


Example 2:

Input:
string = 'banana' 
n=3 

Output:
output = {'ban':1, 'ana':2, 'nan':1}
"""

from collections import defaultdict
from typing import Dict
def get_ngrams(n: int, string: str) -> Dict[str, int]:
    if not string: return {}
    
    ngram_ct = defaultdict(int)
    for i in range(len(string) - n + 1):
        ngram = string[i:i + n]
        ngram_ct[ngram] += 1
    
    return ngram_ct