class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        a=set()
        flc=0
        lc=0
        while j<n:
            if s[j] not in a:
                a.add(s[j])
                lc+=1
                flc=max(lc,flc)
                j+=1
            else:
                a.remove(s[i])
                lc-=1
                i+=1
        return flc