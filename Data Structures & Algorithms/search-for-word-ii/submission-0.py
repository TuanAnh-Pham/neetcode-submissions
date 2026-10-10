

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word:str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        #put 
        for w in words:
            root.addWord(w)
        
        maxRow, maxCol = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or r >= maxRow \
                or c < 0 or c >=maxCol \
                or (r,c) in visit \
                or board[r][c] not in node.children
                ):
                return 
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(maxRow):
            for c in range(maxCol):
                dfs(r,c,root,'')
        
        return list(res)