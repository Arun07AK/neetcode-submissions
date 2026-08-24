class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj=[[] for _ in range(n)]
        #building the graph
        for in_node,out_node in edges:
            adj[in_node].append(out_node)
            adj[out_node].append(in_node)
        #now the conditions to be satisfied has to be checked 
        #condition 1:fully connected 
        #which means , dfs/bfs from one node of graph should be able to reach all nodes from 0 to n-1
        seen=set()
        def dfs(node):
            seen.add(node)
            for neighbor in adj[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        dfs(0)
        if len(seen)==n:
            return True
        else:
            return False

