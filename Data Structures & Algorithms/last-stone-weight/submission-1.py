class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxheap=[]
        for stone in stones:
            self.maxheap.append(-stone)
        heapq.heapify(self.maxheap)
        while(len(self.maxheap)>=2):
            stone_x=heapq.heappop(self.maxheap)
            stone_y=heapq.heappop(self.maxheap)
            if stone_x!=stone_y:
                heapq.heappush(self.maxheap,stone_x-stone_y)
        if self.maxheap:
            return -self.maxheap[0]
        else:
            return 0
        


