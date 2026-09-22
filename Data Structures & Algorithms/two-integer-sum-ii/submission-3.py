class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        i=0
        j=len(n)-1
        while i <j:
            sum=n[i]+n[j]
            if sum==t:
                return [i+1,j+1]
            elif sum<t:
                i+=1
            else:
                j-=1
