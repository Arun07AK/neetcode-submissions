class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        t=1
        for i in nums:
            prefix.append(t)
            t*=i
        res=[]
        pt=1
        postfix=[]
        for i in range(len(nums)-1,-1,-1):
            postfix.append(pt)
            pt*=nums[i]
        postfix.reverse()
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res

        
            
            
            