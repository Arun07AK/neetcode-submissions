class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #adj[crs] stores the immeadiate prerequisite of crs
        adj=[[]for _ in range(numCourses)]
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        #memo[(u,v)] caches that u is a pre req of v
        memo={}
        def dfs(u,curr):
            #memoization/caching
            if (u,curr) in memo:
                return memo[(u,curr)]
            #direct prerequisite
            if u in adj[curr]:
                memo[(u,curr)]=True
                return True
            #indirect prerequisite: we need to recurse
            for pre in adj[curr]:
                if dfs(u,pre):
                    memo[(u,curr)]=True
                    return True
            memo[(u,curr)]=False
            return False

        res=[]
        for querie in queries:
            res.append(dfs(querie[0],querie[1]))
        return res

        
        