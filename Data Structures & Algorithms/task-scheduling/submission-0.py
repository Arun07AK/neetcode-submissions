from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            count[task]=count.get(task,0)+1
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        currtime =0
        q=deque()
        s=0
        while max_heap or q :
            currtime+=1
            if max_heap:
                now=heapq.heappop(max_heap)
                if now+1<0:
                    q.append([now+1,currtime+n])
            if q and q[0][1]==currtime:
                task=q.popleft()[0]
                heapq.heappush(max_heap,task)
        return currtime
            

        
