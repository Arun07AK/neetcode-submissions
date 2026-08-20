from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q=deque()
        seen=set()
        q.append("0000")
        seen.add("0000")
        deadends_hash=set(deadends)
        def bfs(q):
            level=0
            while q:
                for _ in range(len(q)):
                    node=q.popleft()
                    if node==target:
                        return level
                    #loop for different combinations on each index of the string +1 and -1 . which is totally 8 combinations
                    for i in range(len(node)):
                        d=node[i]
                        #+1
                        comb=node[:i]+str((int(d)+1)%10)+node[i+1:]
                        if comb not in deadends_hash and comb not in seen:
                            q.append(comb)
                            seen.add(comb)
                        #-1
                        comb=node[:i]+str((int(d)-1)%10)+node[i+1:]
                        if comb not in deadends_hash and comb not in seen:
                            q.append(comb)
                            seen.add(comb)        
                level+=1
            return -1
        return bfs(q)




        
        