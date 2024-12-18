import heapq
from typing import List


def list_fifths(numlists: List[List[int]]) -> List[int]:
    # first tempt took 6 min
    """
    n: size of each list, k: number of lists
    time = O(k * n * log n) + O(k * log k) ~= O(k * n * log n)
    space = O(k)
    """
    if not numlists: return []

    fifth_num_list = []
    for item in numlists:
        curr_list_sorted = sorted(item, reverse=True)
        fifth_num_list.append(curr_list_sorted[4])

    fifth_num_list.sort()
    return fifth_num_list

# second tempt 16 not done
# third tempt 12 min



def list_fifths(numlists: List[List[float]]) -> List[float]:
    """
    n: size of list, k: number of lists
    
    manually fix heap size:
    time = O(k * n * log 5) + O(k * log k) ~= O(k * n)
    space = O(5) + O(k) ~= O(k)
    """
    if not numlists: return []

    fifth_nums_list = []
    for nums in numlists:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > 5:
                heapq.heappop(min_heap)
        
        fifth_nums_list.append(heapq.heappop(min_heap))
    
    fifth_nums_list.sort()
    return fifth_nums_list


def list_fifths(numlists: List[List[float]]) -> List[float]:
    if not numlists: return []
    
    fifth_nums_list = []
    for nums in numlists:
        top_five_nums = heapq.nlargest(5, nums)
        fifth_nums_list.append(top_five_nums[-1])
    
    fifth_nums_list.sort()
    return fifth_nums_list