import random
import numpy as np
import matplotlib.pyplot as plt


def generate_maze(n):
    maze = np.zeros((n, n), dtype=int)
    visited = [[False for j in range(n)] for i in range(n)]
    stack = []

    start_i, start_j = random.randint(0, n - 1), random.randint(0, n - 1)
    visited[start_i][start_j] = True
    stack.append((start_i, start_j))

    while stack:
        i, j = stack[-1]
        unvisited_neighbours = []
        if i > 0 and not visited[i - 1][j]:
            unvisited_neighbours.append((i - 1, j))
        if i < n - 1 and not visited[i + 1][j]:
            unvisited_neighbours.append((i + 1, j))
        if j > 0 and not visited[i][j - 1]:
            unvisited_neighbours.append((i, j - 1))
        if j < n - 1 and not visited[i][j + 1]:
            unvisited_neighbours.append((i, j + 1))

        if unvisited_neighbours:
            next_i, next_j = random.choice(unvisited_neighbours)
            if random.random() < 0.7:
                visited[next_i][next_j] = True
                stack.append((next_i, next_j))
            else:
                maze[next_i][next_j] = 1
        else:
            stack.pop()

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                start_i, start_j = i, j
                break

    stack = []
    visited = [[False for j in range(n)] for i in range(n)]
    visited[start_i][start_j] = True
    stack.append((start_i, start_j))

    while stack:
        i, j = stack[-1]
        unvisited_neighbours = []
        if i > 0 and not visited[i - 1][j]:
            unvisited_neighbours.append((i - 1, j))
        if i < n - 1 and not visited[i + 1][j]:
            unvisited_neighbours.append((i + 1, j))
        if j > 0 and not visited[i][j - 1]:
            unvisited_neighbours.append((i, j - 1))
        if j < n - 1 and not visited[i][j + 1]:
            unvisited_neighbours.append((i, j + 1))

        if unvisited_neighbours:
            next_i, next_j = random.choice(unvisited_neighbours)
            visited[next_i][next_j] = True
            stack.append((next_i, next_j))
        else:
            stack.pop()
    maze[0][0] = 0
    maze[n-1][n-1] = 0
    return maze
