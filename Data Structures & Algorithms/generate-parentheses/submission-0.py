class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=[]
        def dfs(openc,close):
            if openc==close==n:
                res.append("".join(s))
                return 

            if openc <n:
                s.append("(")
                dfs(openc+1,close)
                s.pop()
            
        
            if close<openc:
                s.append(")")
                dfs(openc,close+1)
                s.pop()
        dfs(0,0)
        return res  
        
        