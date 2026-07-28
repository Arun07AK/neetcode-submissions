class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        cmap={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits)==0:
            return []
        def dfs(index,comb):
            if index ==len(digits):
                res.append("".join(comb))
                return
            choices=cmap[digits[index]]
            for i in choices:
                comb.append(i)
                dfs(index+1,comb)
                comb.pop()
        dfs(0,[])
        return res
        