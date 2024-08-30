from typing import Optional


class Heap:
    """Implementation of Heap (min Heap)
    
    Heap is a data structure which is a complete binary tree, and has the two properties:
        1. Structure property
        2. Order property
    
    Heap can be implemented using array, where the root value is starting with index one not zero.
    """
    
    def __init__(self) -> None:
        self.heap = [0]  # it's a dummy value
    
    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1  # idx is the index of new value inserted
        
        # Need to satisfy order property after insertion.
        while idx > 1 and self.heap[idx // 2] > self.heap[idx]:
            self.heap[idx // 2], self.heap[idx] = self.heap[idx], self.heap[idx // 2]
            idx //= 2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        
        if len(self.heap) == 2:
            return self.heap.pop()
        
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        idx = 1
        while (2 * idx) < len(self.heap):  # this loop condition is check whether there's a left child
            
            # this condition is check whether there's a right child
            if ((2 * idx + 1) < len(self.heap) and
                self.heap[2 * idx + 1] < self.heap[2 * idx] and  # check right child is less than left child
                self.heap[1] > self.heap[2 * idx + 1]):  # check root node is greater than its right child
                
                # swap right child
                self.heap[1], self.heap[2 * idx + 1] = self.heap[2 * idx + 1], self.heap[1]
                
                # update the pointer to right child
                idx = 2 * idx + 1
            
            elif self.heap[1] > self.heap[2 * idx]:
                # swap left child
                self.heap[1], self.heap[2 * idx] = self.heap[2 * idx], self.heap[1]
                
                # update the pointer to left child
                idx = 2 * idx
            
            else:
                break
        
        return result