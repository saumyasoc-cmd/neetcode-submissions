class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a={}
        for char in s:
            a[char] = a.get(char, 0) + 1
        b={}
        for char in t:
            b[char] = b.get(char, 0) + 1
        return a == b