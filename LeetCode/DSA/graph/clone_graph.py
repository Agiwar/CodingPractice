from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """
        deep copy an undirected graph, edges go both ways so there're cycles,
            using BFS with a hashmap from val to cloned node as visited set,
            create the clone when enqueue, so each node only gets queued once,
            then link the cloned neighbor to the current clone for every edge

        keying by val is fine here since vals are unique by constraints,
            in general should key by node itself

        time = O(V + E), each node dequeued once, each edge scanned once
        space = O(V), hashmap and queue
        """

        if not node:
            return None
        
        cloned_status = {node.val: Node(node.val)}
        uncloned_queue = deque([node])
        
        while uncloned_queue:
            uncloned_node = uncloned_queue.popleft()
            
            for neighbor in uncloned_node.neighbors:
                if neighbor.val not in cloned_status:
                    uncloned_queue.append(neighbor)
                    cloned_status[neighbor.val] = Node(neighbor.val)
                
                cloned_status[uncloned_node.val].neighbors.append(cloned_status[neighbor.val])
        
        return cloned_status[node.val]


cloneGraph = Solution().cloneGraph

def test_cloneGraph():
    # LeetCode Example 1: adjList = [[2,4],[1,3],[2,4],[1,3]]
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    clone = cloneGraph(n1)
    assert clone.val == 1
    assert clone is not n1
    assert len(clone.neighbors) == 2
    assert clone.neighbors[0].val == 2
    assert clone.neighbors[1].val == 4

    # LeetCode Example 2: single node
    n1 = Node(1)
    clone = cloneGraph(n1)
    assert clone.val == 1
    assert clone is not n1
    assert clone.neighbors == []

    # LeetCode Example 3: empty graph
    assert cloneGraph(None) == None

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_cloneGraph()
