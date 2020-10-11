def print_spiral_order(mat):
    top = left = 0
    btm = len(mat) - 1
    right = len(mat[0]) - 1

    while True:

        if left > right:
            break

        for i in range(left, right + 1):
            print(mat[top][i])
        top = top + 1

        if top > btm:
            break

        for i in range(top, btm + 1):
            # print(i,right,"hih")
            print(mat[i][right])
        right -= 1

        if left > right:
            break
        for i in range(right, left - 1, -1):
            print(mat[btm][i])
        btm -= 1

        if top > btm:
            break

        for i in range(btm, top - 1, -1):
            print(mat[i][left])
        left += 1


def assign_zero(mat):
    """"?????????????////
    """
    pass


def findPaths(mat, path, i, j):
    (M, N) = (len(mat), len(mat[0]))

    # if we have reached the last cell, print the route
    if i == M - 1 and j == N - 1:
        print(path + [mat[i][j]])
        return

    # include current cell in path
    path.append(mat[i][j])

    # move right
    if 0 <= i < M and 0 <= j + 1 < N:
        findPaths(mat, path, i, j + 1)

    # move down
    if 0 <= i + 1 < M and 0 <= j < N:
        findPaths(mat, path, i + 1, j)

    # remove current cell from path
    # print("path",)
    path.pop()


# print("path22",path)

def count_num_path(m, n):
    if m == 1 or n == 1:
        return 1

    return count_num_path(m, n - 1) + count_num_path(m - 1, n)


def count_dp(m, n):
    """"Count all possible paths from top left to bottom right of a mXn matrix
    """
    count = [[0 for i in range(m)] for j in range(n)]

    for i in range(m):
        count[i][0] = 1
    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]

    return count[m - 1][n - 1]


def matrix(mat):
    """"# Iterative function to find the minimum cost to traverse from the
# first cell to last cell of a matrix
    """
    pass


def matrix_multiplication():
    """"
    """
    pass

def rotate_image():
    pass



if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    path = []

    # start from (0, 0) cell
    x = y = 0

    print(count_dp(3, 3))
