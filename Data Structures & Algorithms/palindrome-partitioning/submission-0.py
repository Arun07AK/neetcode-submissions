class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[] #current partition we are building 
        def dfs(start):
            #base case 1: when we have reached the end of the string
            if start==len(s) :
                res.append(path.copy())
                return 
            #explore every possible substring starting at start 
            for end in range(start,len(s)):
                piece=s[start:end+1]
                if not self.is_pali(piece):
                    continue
                path.append(piece)
                dfs(end+1)
                path.pop()
        dfs(0)
        return res
    def is_pali(self,t):
        return t==t[::-1]