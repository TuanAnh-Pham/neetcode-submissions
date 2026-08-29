class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charDict = {}
        res = 0 
        currMax = 0 

        for r in range(len(s)):
            charDict[s[r]] = 1 + charDict.get(s[r],0)
            currMax = max(currMax,charDict[s[r]])

            while (r-l+1) - currMax > k:
                charDict[s[l]] -= 1
                l += 1

            res = max(res,r-l+1)

        return res