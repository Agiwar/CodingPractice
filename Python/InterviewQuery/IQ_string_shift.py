def can_shift(A: str, B: str) -> bool:
    """
    time = O(n^2)
        • for loop is O(n)
        • string Concatenation is O(n)
                
    space = O(n)
    """
    if not A or not B or len(A) != len(B): return False
    elif A == B: return True

    return any(A[i:] + A[:i] == B for i in range(1, len(A)))


def can_shift(A: str, B: str) -> bool:
    """
    Concatenating an iterable (e.g., string or list) with itself 
    gives you all possible cyclic rotations of the original iterable by any pivot.
    
    time = O(n)
    space = O(n)
    """
    return False if not A or not B or len(A) != len(B) else B in A + A


def can_shift(A: str, B: str) -> bool:
    return A and B and len(A) == len(B) and B in A + A