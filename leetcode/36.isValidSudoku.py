class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            temp_set = set()
            for k in range(9):
                if board[i][k] == '.':
                    continue
                if board[i][k] in temp_set:
                    return False
                temp_set.add(board[i][k])
            temp_set = set()
            for k in range(9):
                if board[k][i] == '.':
                    continue
                if board[k][i] in temp_set:
                    return False
                temp_set.add(board[k][i])

        for i in range(3):
            for k in range(3):
                temp_set = set()
                for row in range(i * 3, i * 3 + 3):
                    for col in range(k * 3, k * 3 + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in temp_set:
                            return False
                        temp_set.add(board[row][col])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
