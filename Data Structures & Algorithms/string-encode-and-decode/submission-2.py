class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ''
        
        encryp = ''
        for s in strs:
            encryp += str(len(s))
            encryp += ','
        
        encryp += '#'
        for s in strs:
            encryp += s
        # '1,2,3,#wordcansay'
        # '1,#word' 
        return encryp


    def decode(self, s: str) -> List[str]:
        # '1,2,3#wordcan#ay'
        # '1,#word'
        
        if len(s) == 0 :
            return []

        sizeMap = []
        res = []
        i = 0
        # '1,2,3#wordcan#ay'
        while s[i] != '#':
            if s[i] != ',':
                j = i+1
                while s[j] != ',': 
                    j += 1 
                #build map [12,13,1]
                sizeMap.append(int(s[i:j]))
                i = j
            i += 1
        # after getting all text size, i is at the #  
        i+=1 

        for num in sizeMap:
            res.append(s[i:i+num])
            i += num
        return res
