class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sn=nums
        n=len(nums)
        rs=[]
        for i in range(n-1):
            if (i>0 and sn[i]==sn[i-1]):
                continue
            j=i+1
            k=n-1
            t=0-sn[i]
            while (j<k):
                if (sn[j]+sn[k]==t):
                    rs.append([sn[i],sn[j],sn[k]])
                    j+=1
                    k-=1
                    while j<k and (sn[j]==sn[j-1]):
                        j=j+1
                    while j<k and (sn[k]==sn[k+1]):
                        k=k-1
                elif sn[j]+sn[k]>t:
                    k=k-1
                else:
                    j+=1

        return rs
        