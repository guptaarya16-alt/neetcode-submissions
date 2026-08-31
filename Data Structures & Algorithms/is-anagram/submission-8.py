class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sone={}
        stwo={}
        count1=0
        count2=0
        for char in s:
            if char in sone:
                sone[char] += 1
            else:
                sone[char]=1
        for char in t:
            if char in stwo:
                stwo[char] += 1
            else:
                stwo[char]=1   
        if sone==stwo:
            return True
        else:
            return False

        
        