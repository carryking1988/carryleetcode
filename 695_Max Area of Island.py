# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.


# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]


def maxAreaOfIsland(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                stack = [(i, j)]
                grid[i][j] = 0
                cnt = 0
                while stack:
                    node = stack[-1]
                    neibors = [
                        (max(node[0] - 1, 0), node[1]),
                        (min(node[0] + 1, m - 1), node[1]),
                        (node[0], max(node[1] - 1, 0)),
                        (node[0], min(node[1] + 1, n - 1))
                    ]
                    pop_flag = True
                    for neibor in neibors:
                        if grid[neibor[0]][neibor[1]] == 1:
                            stack.append(neibor)
                            grid[neibor[0]][neibor[1]] = 0
                            pop_flag = False
                            break
                    if pop_flag:
                        stack.pop()
                        cnt += 1
                res = max(res, cnt)
    return res


print(maxAreaOfIsland(grid))


def myFunc(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                stack = [(i, j)]
                grid[i][j] = 0
                cnt = 0
                while stack:
                    node = stack[-1]
                    neighbors = [
                        (max(node[0] - 1, 0), node[1]),
                        (min(node[0] + 1, m - 1), node[1]),
                        (node[0], max(node[1] - 1, 0)),
                        (node[0], min(node[1] + 1, n - 1)),
                    ]
                    flag = True
                    for neighbor in neighbors:
                        if grid[neighbor[0]][neighbor[1]] == 1:
                            stack.append(neighbor)
                            grid[neighbor[0]][neighbor[1]] = 0
                            flag = False
                            break
                    if flag:
                        stack.pop()
                        cnt += 1
                res = max(res,cnt)
    return res

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
print(myFunc(grid))