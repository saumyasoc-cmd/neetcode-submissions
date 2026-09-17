class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        if len(s)!=len(t):
            return False    
        for char in s:
            sd[char]=sd.get(char,0)+1
        for char in t:
            td[char]=td.get(char,0)+1
        return sd==td      