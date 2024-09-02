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
        
        return
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        
        if len(self.heap) == 2:
            return self.heap.pop()
        
        result = self.heap[1]          # the first value is what we want
        self.heap[1] = self.heap.pop() # to keep heap structure order, the popped value is replaced with last value
        
        i = 1  # pointer of root node
        while (2 * i) < len(self.heap):  # this loop condition is check whether there's a left child
            
            # this condition is check whether there's a right child
            if ((2 * i + 1) < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and  # check right child is less than left child
                self.heap[1] > self.heap[2 * i + 1]):  # check root node is greater than its right child
                
                # swap right child
                self.heap[1], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[1]
                
                # update the pointer to right child
                i = 2 * i + 1
            
            elif self.heap[1] > self.heap[2 * i]:
                # swap left child
                self.heap[1], self.heap[2 * i] = self.heap[2 * i], self.heap[1]
                
                # update the pointer to left child
                i = 2 * i
            
            else:
                break
        
        return result
    
    def heapify(self, arr):
        # move the first value into the last index
        arr.append(arr[0])
        self.heap = arr
        
        curr_idx = (len(self.heap) - 1) // 2  # pointer of the first non-leaf node
        while curr_idx > 0:
            i = curr_idx
            
            while (2 * i) < len(self.heap):
                if ((2 * i + 1) < len(self.heap) and
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[i] > self.heap[2 * i + 1]):
                    
                    # swap right child
                    self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                    
                    # update the pointer to right child
                    i = 2 * i + 1
                
                elif self.heap[i] > self.heap[2 * i]:
                    # swap left child
                    self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                    
                    # update pointer to left
                    i = 2 * i
                
                else:
                    break
            
            curr_idx -= 1
