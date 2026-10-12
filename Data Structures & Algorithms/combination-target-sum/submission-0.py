class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx,currComb,currTotal):
            if currTotal == target:
                res.append(currComb.copy())
                return 
            
            if idx >= len(nums) or currTotal > target:
                return 

            currComb.append(nums[idx])
            
            dfs(idx,currComb,currTotal + nums[idx])
            currComb.pop()
            dfs(idx+1,currComb,currTotal)
        dfs(0, [], 0)
        return res

