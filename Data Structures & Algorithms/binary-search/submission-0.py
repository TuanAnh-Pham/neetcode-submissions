class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        def search(l, r, nums, target):
            if l > r:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] < target:
                return search(mid + 1, r, nums, target)
            elif nums[mid] > target:
                return search(l, mid-1, nums, target)
            else:
                return mid

        return search(0, n-1, nums, target)
