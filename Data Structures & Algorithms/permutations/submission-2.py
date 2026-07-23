class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        per=[]
        used=[False]*len(nums)
        def dfs(per): 
            if len(per)==len(nums):
                res.append(per.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
    
                per.append(nums[j])
                used[j]=True
                dfs(per)
                per.pop()
                used[j]=False
        dfs([])
        return res
                

        