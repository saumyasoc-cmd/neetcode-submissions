class Solution:
    def maxArea(self, n: List[int]) -> int:
        v=0
        mv=0
        i=0
        j=len(n)-1
        while(i<j):
            if n[i]<n[j]:
                v=n[i]*(j-i)
                mv=max(v,mv)
                i+=1
            elif n[i]>n[j]:
                v=n[j]*(j-i)
                mv=max(v,mv)
                j-=1
            else:
                v=n[i]*(j-i)
                mv=max(v,mv)
                i+=1
                j-=1
        return mv
            
            