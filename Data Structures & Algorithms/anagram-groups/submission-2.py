class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            count={}
            for c in s:
                count[c]=count.get(c,0)+1
            key=tuple(sorted(count.items()))
            if key in ans:
                ans[key].append(s)
            else:
                ans[key]=[s]
            
        return list(ans.values())
