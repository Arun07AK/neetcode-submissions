class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        m={}
        for i in range(1,n+1):
            m[i]=[0,0]
        for start,end in trust:
            m[start][0]+=1
            m[end][1]+=1
        for label,count in m.items():
            if count[0]==0 and count[1]==n-1:
                return label
        return -1


        