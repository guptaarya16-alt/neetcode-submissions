class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts={}
        for num in nums:
            if num not in counts:
                #add it and make the count one:
                counts[num]=0
            counts[num]+=1
            

            ##return k most count
        sortkeys=sorted(counts,key=counts.get, reverse=True)
        return sortkeys[:k]


        