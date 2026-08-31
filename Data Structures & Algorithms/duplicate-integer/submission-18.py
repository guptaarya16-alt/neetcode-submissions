class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listtwo=[]
        for i in range(len(nums)):
            if nums[i] in listtwo:
                return True
            else:
                listtwo.append(nums[i])
        else:
            return False