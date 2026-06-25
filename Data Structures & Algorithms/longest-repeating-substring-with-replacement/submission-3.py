class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        length=0
        count={}
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxf=max(maxf,count[s[r]])
            replacement_needed=(r-l+1)-maxf
            if replacement_needed>k:
                #window not acceptable , so we shift
                count[s[l]]-=1
                l+=1
     
            windowsize=(r-l+1)
            length=max(length,windowsize)
            

        return length
