class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0 
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            currMax = max(currMax, r-l+1)
        
        return currMax