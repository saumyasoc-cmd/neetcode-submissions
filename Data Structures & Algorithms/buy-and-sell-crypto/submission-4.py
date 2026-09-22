class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mp=0
        i=0
        j=i+1
        while(j<n):
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                mp=max(mp,prices[j]-prices[i])
                j+=1
        return mp


