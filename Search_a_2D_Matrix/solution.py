class Solution(object):
    if not matrix:
        return 0
    count = 0
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            count += 1
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return count
