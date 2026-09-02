class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        res=0
        adj=[[] for _ in range(n)]
        #building the graph
        for out_node, in_node in edges:
            adj[out_node].append(in_node)
            adj[in_node].append(out_node)
        def dfs(node):
            visited.add(node)
            for neighour in adj[node]:
                if neighour not in visited:
                    dfs(neighour)
        for i in range(n):
            if i not in visited:    
                dfs(i)
                res+=1
        return res


        