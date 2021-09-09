def solution(matrix):
    res = []
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    while left <= right and top <= bottom:
        res.extend(matrix[top][left:right + 1])
        for i in range(top + 1, bottom + 1):
            res.append(matrix[i][right])
        if left < right and top < bottom:
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom - 1, top, -1):
                res.append(matrix[i][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return res


def gen_matrix(row, col):
    matrix = [[0 for _ in range(col)] for _ in range(row)]
    left = 0
    right = col - 1
    top = 0
    bottom = row - 1
    a = 0
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = a
            a += 1
        for i in range(top + 1, bottom + 1):
            matrix[i][right] = a
            a += 1
        if left < right and top < bottom:
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = a
                a += 1
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = a
                a += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return matrix


matrix = gen_matrix(5, 5)
print(matrix)
print(matrix[1:4][1:3])
