class Solution:
    def trap(self, h: List[int]) -> int:
        pm=[0]*len(h)
        sm=[0]*len(h)
        n=len(h)
        pm[0]=h[0]
        sm[n-1]=h[n-1]
        for i in range(n-2,-1,-1):
            sm[i]=(max(h[i],sm[i+1]))
        for i in range(1,n):
            pm[i]=(max(h[i],pm[i-1]))
        v=0
        for i in range(n):
            lm=pm[i]
            rm=sm[i]
            if h[i]<lm and h[i]<rm:
                v+=min(lm,rm)-h[i]
        return v
        
