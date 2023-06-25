# Written by *** for COMP9021
#
# Implements a function display_leftmost_topmost_boundary(*grid)
# whose argument grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# that represent one or more "full polygons" that do not "touch"
# each other.
# The selected polygon's top boundary is as high as possible ,
# and amongst all polygons whose top boundary is as high as possible,
# the selected polygon's top boundary starts as much to the left
# as possible.


def display(*grid):
    for e in grid:
        print(*e)


directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def check_neighbour_points(grid, cur_x, cur_y, value):
    result = []
    for dir_x, dir_y in directions:
        row, col = cur_x + dir_x, cur_y + dir_y
        if 0 <= row < len(grid[0]) and 0 <= col < len(grid):
            if grid[col][row] == value:
                result.append((row, col))
    return result


def dfs(grid, cur_x, cur_y, visited):
    if (cur_x, cur_y) in visited:
        return
    grid[cur_y][cur_x] = ' '
    visited.append((cur_x, cur_y))

    points = check_neighbour_points(grid, cur_x, cur_y, '*')
    for x, y in points:
        dfs(grid, x, y, visited)


def visited_points(*grid):
    temp_grid = [list(line) for line in grid]
    all_points = []
    for y in range(len(temp_grid)):
        for x in range(len(temp_grid[0])):
            if temp_grid[y][x] == '*':
                visited = []
                dfs(temp_grid, x, y, visited)
                all_points.append(visited)
    return all_points


def display_leftmost_topmost_boundary(*grid):
    # REPLACE PASS ABOVE WITH YOUR CODE
    new_grid = [list(line) for line in grid]
    all_visited = visited_points(*grid)
    if all_visited:
        boundary_points = []
        for cur_x, cur_y in all_visited[0]:
            count = 0
            for dir_x, dir_y in directions:
                next_x, next_y = cur_x + dir_x, cur_y + dir_y
                if (next_x, next_y) in all_visited[0]:
                    count += 1
            if count == 4:
                continue
            else:
                boundary_points.append((cur_x, cur_y))

        for y in range(len(new_grid)):
            line = []
            for x in range(len(new_grid[0])):
                if (x, y) in boundary_points:
                    line.append('*')
                else:
                    line.append(' ')
            print(' '.join(line))
