import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(-freq,num))
        my_list=[]
        for i in range(k):
            my_list.append(heapq.heappop(heap)[1])
        return my_list
            

