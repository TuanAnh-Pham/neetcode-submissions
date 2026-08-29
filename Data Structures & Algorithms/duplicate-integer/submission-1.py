class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        i = 0
        while i < len(nums):
            if nums[i] not in res :
                res[nums[i]] = 1
            else:
                return True
            i+=1
        return False 