class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        square = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(len(board[0])):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue

                if board[r][c] in square[(r // 3, c // 3)] or board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False

                square[(r // 3, c // 3)].add(board[r][c])
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
        return True



        
        