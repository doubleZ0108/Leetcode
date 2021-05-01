#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag_board = [0 for _ in range(10)]

        for i in range(9):
            flag_board = [0 for _ in range(10)]
            for j in range(9):
                content = board[i][j]
                if content != '.':
                    flag_board[int(content)] += 1
                    if flag_board[int(content)] > 1:
                        return False
        for j in range(9):
            flag_board = [0 for _ in range(10)]
            for i in range(9):
                content = board[i][j]
                if content != '.':
                    flag_board[int(content)] += 1
                    if flag_board[int(content)] > 1:
                        return False
        for ii in range(3):
            for jj in range(3):
                flag_board = [0 for _ in range(10)]
                for i in range(ii*3, ii*3 + 3):
                    for j in range(jj*3, jj*3 + 3):
                        content = board[i][j]
                        if content != '.':
                            flag_board[int(content)] += 1
                            if flag_board[int(content)] > 1:
                                return False
        return True
# @lc code=end

