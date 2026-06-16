class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_chars={}
        for i in s:
            if i in seen_chars:
                seen_chars[i]+=1
            else:
                seen_chars[i]=1
        seen_chars2={}
        for j in t:
            if j in seen_chars2:
                seen_chars2[j]+=1
            else:
                seen_chars2[j]=1
        if seen_chars==seen_chars2:
            return True
        else:
            return False
        

        