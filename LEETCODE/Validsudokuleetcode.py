class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for i in range(9):
            for j in range(9):
                cur_ele = board[i][j]
                if cur_ele != ".":
                    row = (cur_ele) + " row " + str(i)
                    col = cur_ele + " col " + str(j)
                    box = cur_ele + " box " + str(i//3) + str(j//3)
                    
                    if row in seen or col in seen or box in seen:
                        return False
                    
                    seen[col] = True
                    seen[row] = True
                    seen[box] = True
        
        return True
