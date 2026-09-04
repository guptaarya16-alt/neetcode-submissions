class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i in range(len(nums)):
            bingo=target-nums[i]
            if bingo in store:
                return [store[bingo], i]
            else:
                store[nums[i]]=i

                    

        