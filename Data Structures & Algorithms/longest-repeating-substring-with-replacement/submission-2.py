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
            while replacement_needed>k:
                #window not acceptable , so we skrink
                count[s[l]]-=1
                l+=1
                replacement_needed=(r-l+1)-maxf
                
            windowsize=(r-l+1)
            length=max(length,windowsize)
            

        return length
