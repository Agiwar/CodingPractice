from typing import Dict


def search_list(target: int, linked_list: Dict[str, Dict]) -> bool:
    # {value: 1, next: {value: 2, next: {value: 3, next: {4, next: {value: 5, next: None}}}}}
    if not linked_list: return False
    
    curr = linked_list
    while curr:
        if curr["value"] == target:
            return True
        
        curr = curr["next"]
    
    return False