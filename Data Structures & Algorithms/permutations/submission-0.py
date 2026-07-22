class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        per=[]
        def dfs(i,per): 
            if len(per)==len(nums):
                res.append(per.copy())
                return
            for j in range(0,len(nums)):
                if nums[j] in per:
                    continue
                per.append(nums[j])
                dfs(0,per)
                per.pop()
        dfs(0,[])
        return res
                

        