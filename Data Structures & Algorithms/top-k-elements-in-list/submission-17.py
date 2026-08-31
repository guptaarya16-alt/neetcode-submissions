class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        bucket = [[]for j in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        result=[]
        for p in range(len(bucket)-1,-1,-1): ## saying start looping at last index of bucket, go all the way to end (index 0) and go down by 1. 
            for num in bucket[p]:
                result.append(num)
                if len(result) == k:
                   return result 

                
    
        
            

        