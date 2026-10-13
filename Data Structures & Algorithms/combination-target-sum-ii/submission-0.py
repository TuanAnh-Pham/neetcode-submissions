class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx,comb,total):
            if total == target:
                res.append(comb.copy())
                return
            
            if total > target or idx == len(candidates):
                return
            
            comb.append(candidates[idx])
            dfs(idx+1,comb,total+candidates[idx])
            comb.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1,comb,total)

        dfs(0,[],0)
        return res

        