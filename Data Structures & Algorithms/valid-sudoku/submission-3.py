from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        squareCheck = defaultdict(set)

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rowCheck[r] or \
                        board[r][c] in colCheck[c] or \
                        board[r][c] in squareCheck[r//3,c//3]
                        ):
                    return False
                else:
                  rowCheck[r].add(board[r][c])
                  colCheck[c].add(board[r][c])  
                  squareCheck[r//3,c//3].add(board[r][c])
        return True

                    