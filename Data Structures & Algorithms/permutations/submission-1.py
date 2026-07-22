class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        per=[]
        def dfs(per): 
            if len(per)==len(nums):
                res.append(per.copy())
                return
            for j in range(len(nums)):
                if nums[j] in per:
                    continue
                per.append(nums[j])
                dfs(per)
                per.pop()
        dfs([])
        return res
                

        