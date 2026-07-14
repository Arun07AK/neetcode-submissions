class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for stone in stones:
            maxheap.append(-stone)
        heapq.heapify(maxheap)
        while(len(maxheap)>=2):
            stone_x=heapq.heappop(maxheap)
            stone_y=heapq.heappop(maxheap)
            if stone_x!=stone_y:
                heapq.heappush(maxheap,stone_x-stone_y)
        if maxheap:
            return -maxheap[0]
        else:
            return 0
        


