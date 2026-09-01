class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new=set(nums)
        streak=1
        longest=0
        for i in new:
            if i-1 in new:
                continue
            else:
                start = i
            while start+1 in new:
                start+=1
                streak+=1
            longest = max(longest, streak)
            streak=1 
        return longest
            

            

        