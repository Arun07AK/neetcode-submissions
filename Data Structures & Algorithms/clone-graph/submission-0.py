"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        old_to_new={node:Node(node.val)}
        frontier=[node]
        while frontier:
            curr=frontier.pop()
            for nxt in curr.neighbors:
                if nxt not in old_to_new:
                    old_to_new[nxt]=Node(nxt.val)
                    frontier.append(nxt)
                old_to_new[curr].neighbors.append(old_to_new[nxt])
        return old_to_new[node]
        