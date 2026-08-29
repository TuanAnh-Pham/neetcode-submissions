class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        nonAlpha = "`!@#$%?' "
        while start < end:
            while not s[start].isalnum() and start < end :
                start +=1
            while not s[end].isalnum() and start < end:
                end -= 1

            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        
        return True