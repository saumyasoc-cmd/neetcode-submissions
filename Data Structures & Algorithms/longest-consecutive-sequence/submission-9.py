class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn=set(nums)
        longest=0
        for n in setn:
            if n-1 not in setn:
                length=1
                while n+length in setn:
                    length+=1
                longest=max(length,longest)
        return longest
