class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(idx,subset):
            if idx == len(nums):
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[idx])
            dfs(idx+1,subset)
            subset.pop()
            dfs(idx+1,subset)
        nums.sort()
        dfs(0,[])
        return [list(s) for s in res]