class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        char_count={}
        #we record all the unique chars in t
        for c in t :
            char_count[c]=1+char_count.get(c,0)
        need=len(char_count)
        window=[l,r]
        window_length=float('inf')
        formed=0
        wc_count={}
        for r in range(len(s)):
            wc_count[s[r]]=1+wc_count.get(s[r],0)
            if s[r] in char_count and char_count[s[r]]==wc_count[s[r]]:
                formed+=1
            while formed==need:
                if r-l+1<window_length:
                    window_length=r-l+1
                    window=[l,r]
                rm=s[l]
                wc_count[s[l]]-=1
                l+=1
                if rm in char_count and char_count[rm]>wc_count[rm]:
                    formed-=1
        if window_length==float('inf'):
            return ""
        return s[window[0]:window[1]+1]
        
                

                
                


            
            