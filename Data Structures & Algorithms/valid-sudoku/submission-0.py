class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quads = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        def get_quad(row, col):
            return (row // 3)*3 + (col // 3)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                q = get_quad(i, j)
                if val == '.':
                    continue
                if val in quads[q]:
                    # print('failed quads', quads)
                    return False
                if val in rows[i]:
                    # print('failed rows', rows)
                    return False
                if val in cols[j]:
                    # print('failed cols', cols)
                    return False
                quads[q].add(val)
                rows[i].add(val)
                cols[j].add(val)
        return True
        