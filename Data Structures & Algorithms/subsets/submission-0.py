class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset[:])
                return 
            #there are 2 ways to branch 
            #one way is including it 
            subset.append(nums[i])
            #and then moving to the next element 
            dfs(i+1)
            #or other way is excluding this element and moving to the next element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

        