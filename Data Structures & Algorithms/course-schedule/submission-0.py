from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #building the graph
        adj=[[] for _ in range(numCourses)]
        in_deg=[0]*numCourses
        for out_node,in_node in prerequisites:
            adj[in_node].append(out_node)
            in_deg[out_node]+=1
        q=deque()
        count=0
        #adding all the nodes with indegree 0 to the queue
        for i in range(numCourses):
            if in_deg[i]==0:
                q.append(i)
        if len(q)==0:
            return False
        while q:
            out_node=q.popleft()
            count+=1
            for neighbor in adj[out_node]:
                in_deg[neighbor]-=1
                if in_deg[neighbor]==0:
                    q.append(neighbor)
        if count==numCourses:
            return True
        return False
        




        
        
                
                
        
            

        