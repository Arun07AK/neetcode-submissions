class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            target=nums[k]
            if target>0:
                break
            l=k+1
            r=len(nums)-1
            
            while(l<r):
                threesum=nums[l]+nums[r]+target
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    res.append([target,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1

    
        return res


        