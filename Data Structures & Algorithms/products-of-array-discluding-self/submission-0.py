class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_list=[]
        for i in range(len(nums)):
            j=i+1
            k=0
            m=1
            while k<i:
                m*=nums[k]
                k+=1
            while j<len(nums):
                m*=nums[j]
                j+=1
            my_list.append(m)
        return my_list
            
            
            