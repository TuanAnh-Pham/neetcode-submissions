class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(comb, pick):
            if len(comb) == len(nums):
                res.append(comb[:])
                return

            for i in range(len(nums)):
                if not pick[i]:
                    comb.append(nums[i])
                    pick[i] = True
                    dfs(comb,pick)
                    comb.pop()
                    pick[i] = False
        
        dfs([],[False]*len(nums))
        return res