class Solution:
    #brute
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for n,i in enumerate(nums):
            diff=target-i
            if diff in mp:
                return [mp[diff],n]
            mp[i]=n

        

        