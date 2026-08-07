class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        omap={}
        for i in range(len(order)):
            omap[order[i]]=i
        
        p=0
        while p<(len(words)-1):
            left=words[p]
            right=words[p+1]
            l=0
            r=0
            is_it_mismatch=False
            while (l<len(left) and r<len(right)):
                if left[l]==right[r]:
                    l+=1
                    r+=1
                elif left[l]!=right[r]:
                    if omap[left[l]]<omap[right[r]]:
                        is_it_mismatch=True
                        break
                    else:
                        return False
            if is_it_mismatch==False and len(right)<len(left):
                return False
            p+=1
        return True





        

        