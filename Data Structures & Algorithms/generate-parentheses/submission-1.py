class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=[]
        def dfs(openc,close):
            if len(s)==2*n:
                res.append("".join(s))
                return 
            #down option A
            if openc <n:
                s.append("(")
                dfs(openc+1,close)
                s.pop()
            #down option B
            if close<openc:
                s.append(")")
                dfs(openc,close+1)
                s.pop()
        dfs(0,0)
        return res  
        
        