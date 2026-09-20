class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp=1
        zc=nums.count(0)
        if zc>1:
            return [0]*len(nums)
        res=[]
        tp=1
        for n in nums:
            if n!=0:
                tp=tp*n
        for n in nums:
            if zc==1:
                if n==0:
                    res.append(tp)
                else:
                    res.append(0)
            else:
                res.append(tp//n)
        return res