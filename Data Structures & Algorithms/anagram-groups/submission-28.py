class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort={}
        for i in strs:
            count=[0]*26
            for char in i:
                index=ord(char)-ord("a")
                count[index]+=1
            key= tuple(count)
            if key in sort:
                sort[key].append(i)
            else:
                sort[key] = [i]
        return list(sort.values())

    
        