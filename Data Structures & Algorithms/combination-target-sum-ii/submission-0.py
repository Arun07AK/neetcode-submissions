class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        candidates.sort()
        def dfs(i,comb,total):
            if total==target:
                res.append(comb.copy())
                return
            if total>target :
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                comb.append(candidates[j])
                dfs(j+1,comb,total+candidates[j])
                comb.pop()
        dfs(0,[],0)
        return res
