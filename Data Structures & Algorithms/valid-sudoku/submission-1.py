class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            seen = set()

            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)


        # Check columns
        for j in range(9):
            seen = set()

            for i in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)


        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                seen = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        num = board[i][j]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True