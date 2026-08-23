class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for i in range(numCourses)]
        q=deque()
        in_deg=[0]*numCourses
        for in_node,out_node in prerequisites:
            adj[out_node].append(in_node)
            in_deg[in_node]+=1
        for i in range(numCourses):
            if in_deg[i]==0:
                q.append(i)
       
        order=[]
        while q:
            node=q.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_deg[neighbor]-=1
                if in_deg[neighbor]==0:
                    q.append(neighbor)
        if len(order)==numCourses:
            return order
        else:
            return []
        
        




        