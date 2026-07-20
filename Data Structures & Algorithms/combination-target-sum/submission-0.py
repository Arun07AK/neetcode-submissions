class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        def dfs(need,i):
            #if the need is satisfied this is a valid combination 
            if need==0:
                res.append(comb.copy())
                return
            if need<0 or i>=len(nums):
                return
            comb.append(nums[i])
            dfs(need-nums[i],i)
            comb.pop()
            dfs(need,i+1)
        dfs(target,0)
        return res
 

        