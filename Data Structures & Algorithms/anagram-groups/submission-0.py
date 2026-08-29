class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for txt in strs:
            sortedTxt = ''.join(sorted(txt))
            res[sortedTxt].append(txt)
        
        return list(res.values())