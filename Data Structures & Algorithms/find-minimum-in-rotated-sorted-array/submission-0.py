class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)//2
            if nums[mid]>nums[h]:
                l=mid+1
            elif nums[mid]<nums[h]:
                h=mid
            else:
                return nums[mid]
        return -1
    


        