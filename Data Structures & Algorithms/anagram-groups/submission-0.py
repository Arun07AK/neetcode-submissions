class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count={}
        result=[]
        for i in strs:
            srtd="".join(sorted(i))
            if srtd in count:
                count[srtd].append(i)
            else:
                count[srtd]=[i]
        return list(count.values())
