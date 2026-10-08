class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currMin = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                currMin = min(currMin, nums[l])
                break
            mid = l + (r-l) //2
            currMin = min(currMin, nums[mid])
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return currMin