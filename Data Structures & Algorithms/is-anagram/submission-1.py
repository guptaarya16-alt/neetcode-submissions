class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        countss={}
        if len(s)==len(t):
            for char in s:
                if char in counts:
                    counts[char]+=1
                else:
                    counts[char]=1
            for char in t:
                if char in countss:
                    countss[char]+=1
                else:
                    countss[char]=1
            if counts == countss:
                return True
            else:
                return False
        else:
            return False

        
        
        

        