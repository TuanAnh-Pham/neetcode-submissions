class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        if len(s) != len(t):
            return False
        else:
            #count number of time each char in s appear
            for c in s:
                if c not in check:
                    check[c] = 1
                else:
                    check[c] +=1
            
            for l in t:
                #return false immediately if not found or over count
                if l not in check or check[l] == 0:
                    return False
                else:
                    check[l]-=1
            return True