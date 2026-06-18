import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        bucket =[[] for i in range(len(nums)+1)]
        for num,frq in count.items():
            bucket[frq].append(num)
        
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)
                if len(result)==k:
                    return result
            
            

