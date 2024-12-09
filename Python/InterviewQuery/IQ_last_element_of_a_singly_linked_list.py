"""
head object example : {"data":1,"next":{"data":2,"next":{"data":3,"next":None}}}
"""
def get_last_node(head: dict) -> list:
    if not head: return None

    while head["next"] is not None:
        head = head["next"]
    
    return head
