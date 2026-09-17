class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values=[(num,i)for i, num in enumerate(nums)]
        values.sort()
        p1=0
        p2=len(values)-1
        for i in range (len(nums)-1):
            if values[p1][0]+values[p2][0]>target:
                p2-=1
            elif values[p1][0]+values[p2][0]<target:
                p1+=1
            else:
                return sorted([values[p1][1],values[p2][1]])
        return []


        