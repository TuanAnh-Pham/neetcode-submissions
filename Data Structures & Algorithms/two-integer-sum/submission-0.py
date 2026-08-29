class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #build hash map
        hmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            # 1 time iterrate to build map with minimum index
            if nums[i] not in hmap:
                hmap[nums[i]] = i
            
            if diff in hmap:
                if hmap[diff] != i:
                    return [hmap[diff],i]
        
