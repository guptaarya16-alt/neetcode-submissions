class Solution:

    def encode(self, strs: List[str]) -> str:
        new=""
        for i in strs:
            new += str(len(i)) + "#" + i
        return new
            


                


    def decode(self, s: str) -> List[str]:
        final=[]
        i=0
        while i < len(s):
            for j in range(i,len(s)):
                if s[j] == "#":
                    length= int(s[i:j])
                    start=j+1
                    end=j+1+length
                    final.append(s[start:end])
                    break
            i=j+1+length
        return final       
        
            