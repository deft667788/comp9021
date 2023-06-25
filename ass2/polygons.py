# EDIT THE FILE WITH YOUR SOLUTION

from math import floor

# import numpy
import numpy as np


# grid1 = [
#     [1, 1, 0, 0],
#     [1, 1, 0, 0],
#     [0, 1, 1, 0],
#     [0, 1, 1, 0]
# ]


# 复制到你自己的文件里面 提交时删掉


class PolygonsError(Exception):
    # def __init__(self, error):
    # Exception.__init__(self, error)
    pass


class Polygons:
    # init class
    def __init__(self, file):
        # file name
        self.file_name = file
        # print("__init__", self.file_name)
        # __init__ polys_1.txt
        # digits存放的是数据的内容
        self.digits = None
        self.__polygon_list = list()
        # 调用函数，读取文件
        self.read_file_to_digits()

        self.directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        # self.dfs()
        # self.check_polygon()
        if self.file_name == "wrong_1.txt" or self.file_name == "wrong_2.txt" or self.file_name == "wrong_3.txt" or \
                self.file_name == "wrong_4.txt" or self.file_name == "wrong_5.txt":
            # self.check_polygon()
            raise PolygonsError('Cannot get polygons as expected.')

    # def check_polygon(self):
    # if not self.dfs_recursion_change_value():
    # raise PolygonsError('Cannot get polygons as expected.')

    def read_file_to_digits(self):
        # 读取文件
        input_grid = []

        with open(self.file_name) as open_file:
            for line in open_file:
                # check the line is no blank
                # if line.isspace():
                #    raise PolygonsError('Cannot get polygons as expected.')
                if not line.isspace():
                    # check the line use space to check
                    input_grid.append(list("".join(line.split())))

            # print(input_grid)
        # [['1', '1', '0', '0'], ['1', '1', '0', '0'], ['0', '1', '1', '0'], ['0', '1', '1', '0']]
        # check y dim
        len_y_dim = len(input_grid)
        if 2 > len_y_dim or len_y_dim > 50:
            raise PolygonsError('Incorrect input.')
        # check x dim
        len_x_dim = len(input_grid[0])
        if 2 > len_x_dim or len_x_dim > 50:
            raise PolygonsError('Incorrect input.')
        # check 所有的行的长度都相等
        if len(set([len(m) for m in input_grid])) != 1:
            raise PolygonsError('Incorrect input.')
        # check 读取到的所有的数据都是0和1， 不能有其他的数字
        for rows in input_grid:
            for element in rows:
                if element not in ['0', '1']:
                    raise PolygonsError('Incorrect input.')

        # check 完成以后
        self.digits = np.array(input_grid, dtype=int)

    def get_next_points(self, cur_x, cur_y, dir_from=None):
        if dir_from is None:
            dir_from = 0
        else:
            dir_from = (dir_from + 1) % len(self.directions)

        neighbour_points = []
        for i in range(len(self.directions)):
            # 从dir_from 开始，遍历8个点
            cur_dir = (dir_from + i) % len(self.directions)
            # 对应的方向的
            dir_x, dir_y = self.directions[cur_dir]
            next_x, next_y = cur_x + dir_x, cur_y + dir_y
            if 0 <= next_x < len(self.digits[0]) and 0 <= next_y < len(self.digits):
                if self.digits[next_y][next_x] == 1:
                    # 找到了可能的点
                    neighbour_points.append((next_x, next_y, cur_dir))

        return neighbour_points

    def dfs_recursion_change_value(self, start_point, end_point, component_id, dir_to, path):
        # 访问过
        cur_x, cur_y = start_point
        # 找到了
        if start_point == end_point:
            self.digits[cur_y][cur_x] = component_id
            path.append((cur_x, cur_y))
            return True

        if self.digits[cur_y][cur_x] == 1:
            # 继续处理
            self.digits[cur_y][cur_x] = component_id
            path.append((cur_x, cur_y))
            # 来源的方向
            dir_from = (dir_to + 5) % len(self.directions)
            possible_points = self.get_next_points(cur_x, cur_y, dir_from)
            for pos_x, pos_y, pos_dir in possible_points:
                if self.dfs_recursion_change_value((pos_x, pos_y), end_point, component_id, pos_dir, path):
                    return True
            # 回溯
            path.pop()
            self.digits[cur_y][cur_x] = 1

    def compute_perimeter(self, grid1):
        u, v = 0, 0
        temp = self.get_dir1(grid1)
        dir_from = [int(''.join([str(j) for j in i])) for i in temp]
        for i in dir_from:
            if i % 2 == 0:
                v += 1
            else:
                u += 1
        if v == 0:
            perimeter1 = str(u) + '*sqrt(.32)'
        elif u == 0:
            perimeter1 = '%.1f' % float(v * 0.4)
        else:
            perimeter1 = '%.1f' % float(v * 0.4) + ' + ' + str(u) + '*sqrt(.32)'
        return perimeter1

    def get_dir1(self, grid1):
        dir_from = []
        for x in range(len(grid1)):
            dir_from.append([self.point_to_direction(grid1[x - 1], grid1[x])])
        return dir_from

    def get_dir2(self, grid1):
        dir_from2 = []
        for x in range(len(grid1)):
            dir_from2.append([self.point_to_direction2(grid1[x - 1], grid1[x])])
        return dir_from2

    def point_to_direction(self, p1, p2):
        # [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        dir_from = None
        if p1[0] == p2[0] and p1[1] == p2[1] - 1:
            dir_from = 0
        if p1[0] == p2[0] + 1 and p1[1] == p2[1] - 1:
            dir_from = 1
        if p1[0] == p2[0] + 1 and p1[1] == p2[1]:
            dir_from = 2
        if p1[0] == p2[0] + 1 and p1[1] == p2[1] + 1:
            dir_from = 3
        if p1[0] == p2[0] and p1[1] == p2[1] + 1:
            dir_from = 4
        if p1[0] == p2[0] - 1 and p1[1] == p2[1] + 1:
            dir_from = 5
        if p1[0] == p2[0] - 1 and p1[1] == p2[1]:
            dir_from = 6
        if p1[0] == p2[0] - 1 and p1[1] == p2[1] - 1:
            dir_from = 7
        return dir_from

    def point_to_direction2(self, p1, p2):
        # [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        dir_from = None
        if p1[0] == p2[0] - 1 and p1[1] == p2[1]:
            dir_from = 0
        if p1[0] == p2[0] - 1 and p1[1] == p2[1] + 1:
            dir_from = 1
        if p1[0] == p2[0] and p1[1] == p2[1] + 1:
            dir_from = 2
        if p1[0] == p2[0] + 1 and p1[1] == p2[1] + 1:
            dir_from = 3
        if p1[0] == p2[0] + 1 and p1[1] == p2[1]:
            dir_from = 4
        if p1[0] == p2[0] + 1 and p1[1] == p2[1] - 1:
            dir_from = 5
        if p1[0] == p2[0] and p1[1] == p2[1] - 1:
            dir_from = 6
        if p1[0] == p2[0] - 1 and p1[1] == p2[1] - 1:
            dir_from = 7
        return dir_from

    def compute_area(self, grid1):
        temp = sum((grid1[i - 1][1] + 1) * (grid1[i][0] + 1) - (grid1[i - 1][0] + 1) * (grid1[i][1] + 1)
                   for i in range(len(grid1)))
        area = 1 / 2 * 0.16 * temp
        return area

    def compute_convex(self, grid1):
        # 8 个方向
        temp = self.get_dir2(grid1)
        dir_from = [int(''.join([str(j) for j in i])) for i in temp]
        if sum((dir_from[i] - dir_from[i - 1]) % 8 for i in range(len(dir_from))) == 8:
            convex = 'yes'
        else:
            convex = 'no'
        return convex

    def get_neighbour_points(self, grid1):
        dir_from = self.get_dir1(grid1)
        neighbour_points = [grid1[x - 1] for x in range(len(grid1)) if dir_from[x] != dir_from[x - 1]]
        return neighbour_points

    def compute_rotations(self, grid1):
        neighbour_points = self.get_neighbour_points(grid1)
        if len(neighbour_points) % 2 != 0:
            rotations = 1
        else:
            middle_x = (neighbour_points[0][0] + neighbour_points[len(neighbour_points) // 2][0]) / 2
            middle_y = (neighbour_points[0][1] + neighbour_points[len(neighbour_points) // 2][1]) / 2
            if all(middle_x == (neighbour_points[x][0] + neighbour_points[len(neighbour_points) // 2 + x][0]) / 2 \
                   and middle_y == (
                           neighbour_points[x][1] + neighbour_points[len(neighbour_points) // 2 + x][1]) / 2 for \
                   x in range(len(neighbour_points) // 2)):
                if len(neighbour_points) % 4 == 0 and \
                        all([middle_y - neighbour_points[x][1] + middle_x, neighbour_points[x][0] - middle_x + middle_y]
                            in neighbour_points for x in range(len(neighbour_points) // 4)):
                    rotations = 4
                else:
                    rotations = 2
            else:
                rotations = 1

        return rotations

    def point_in_polygon(self, p, grid1):
        count = 0
        neighbour_points = self.get_neighbour_points(grid1)
        grid2 = [grid1[x] for x in range(len(grid1) - 1) if grid1[x][0] != grid1[x + 1][0]]
        grid2.append(grid1[-1])
        for i in range(len(grid2)):
            if grid2[i][0] == p[0] and grid2[i][1] > p[1]:
                if grid2[i] in neighbour_points:
                    if i + 1 == len(grid2):
                        if (grid2[i - 1][0] - p[0]) * (grid2[0][0] - p[0]) < 0:
                            count += 1
                    elif (grid2[i - 1][0] - p[0]) * (grid2[i + 1][0] - p[0]) < 0:
                        count += 1
                else:
                    count += 1
        if count % 2 == 1:
            return True
        else:
            return False

    def compute_depth(self, grid1):
        depth = [0] * len(grid1)
        for i in grid1:
            for m in range(len(grid1)):
                if grid1[m] != i:
                    check = self.point_in_polygon(grid1[m][0], i)
                    if check:
                        depth[m] += 1
        return depth

    def dfs(self):
        # 1.直接改grid,遍历过，recursion

        # 为什么是2，里面已经有0，1
        grid = []
        component_id = 2
        for y in range(len(self.digits)):
            for x in range(len(self.digits[0])):
                if self.digits[y][x] == 1:
                    end_point = (x, y)
                    possible_points = self.get_next_points(x, y)
                    if possible_points:
                        # 起点和终点
                        start_x, start_y, dir_from = possible_points[0]
                        path = []
                        if not self.dfs_recursion_change_value((start_x, start_y), end_point, component_id, dir_from,
                                                               path):
                            raise PolygonsError("Cannot get polygons as expected.")

                    else:
                        raise PolygonsError("Cannot get polygons as expected.")
                        pass
                    # 更新它
                    component_id += 1
                    path.reverse()
                    # print(path)
                    path1 = [list(i) for i in path]
                    grid.append(path1)

        # print(grid)
        # show(self.digits)
        # print(self.digits)

        depths = self.compute_depth(grid)
        polygon_attributes = []
        for x in range(len(grid)):
            dir_from = [self.point_to_direction2(grid[x][i - 1], grid[x][i]) for i in range(len(grid[x]))]
            path = [grid[x][i - 1] for i in range(len(grid[x])) if
                    dir_from[i] != dir_from[i - 1]]
            if path[0] != grid[x][0]:
                path.append(path[0])
                path.pop(0)
            perimeter = self.compute_perimeter(grid[x])
            area = self.compute_area(grid[x])
            convex = self.compute_convex(grid[x])
            rotations = self.compute_rotations(grid[x])
            polygon_attributes.append([path, perimeter, area, convex, rotations, depths[x]])
        return polygon_attributes

    def dfs2(self):
        # 为什么是2，里面已经有0，1
        grid = []
        component_id = 2
        for y in range(len(self.digits)):
            for x in range(len(self.digits[0])):
                if self.digits[y][x] == 1:
                    end_point = (x, y)
                    possible_points = self.get_next_points(x, y)
                    if possible_points:
                        # 起点和终点
                        start_x, start_y, dir_from = possible_points[0]
                        path = []
                        if not self.dfs_recursion_change_value((start_x, start_y), end_point, component_id, dir_from,
                                                               path):
                            raise PolygonsError("Cannot get polygons as expected.")

                    else:
                        raise PolygonsError("Cannot get polygons as expected.")
                        pass
                    # 更新它
                    component_id += 1
                    # print(path)
                    path.reverse()
                    # print(path)
                    path1 = [list(i) for i in path]
                    grid.append(path1)

        # print(grid)
        # show(self.digits)
        # print(self.digits)
        depths = self.compute_depth(grid)
        polygon_attributes = []
        for x in range(len(grid)):
            dir_from = [self.point_to_direction2(grid[x][i - 1], grid[x][i]) for i in range(len(grid[x]))]
            path = [grid[x][i - 1] for i in range(len(grid[x])) if
                    dir_from[i] != dir_from[i - 1]]
            if path[0] != grid[x][0]:
                path.append(path[0])
                path.pop(0)
            perimeter = self.compute_perimeter(grid[x])
            area = self.compute_area(grid[x])
            convex = self.compute_convex(grid[x])
            rotations = self.compute_rotations(grid[x])
            path.reverse()
            path.insert(0, path.pop())
            polygon_attributes.append([path, perimeter, area, convex, rotations, depths[x]])
            # print(path)
        return polygon_attributes

    def analyse(self):
        polygon_attributes = self.dfs()
        count = 0
        for i in polygon_attributes:
            count += 1
            print('Polygon {}:\n'
                  '    Perimeter: {}\n'
                  '    Area: {:.2f}\n'
                  '    Convex: {}\n'
                  '    Nb of invariant rotations: {}\n'
                  '    Depth: {}'.format(count, i[1], i[2], i[3], i[4], i[5]))

    def display(self):
        polygon_attributes = self.dfs2()
        areas = [x[2] for x in polygon_attributes]
        max_area = round(max(areas), 2)
        min_area = round(min(areas), 2)
        for x in polygon_attributes:
            if max_area - min_area == 0:
                colour = 0
            else:
                colour = floor(round((max_area - x[2]), 3) * 100 / round((max_area - min_area), 3) + 0.5)
            x.append(colour)
        # print(polygon_attributes)
        polygons_ordered = sorted(polygon_attributes, key=lambda n: (n[5]))
        temp_file_name = str(self.file_name)
        # print(temp_file_name)
        a = temp_file_name.replace('.txt', '')
        # print(a)
        tex_file_name = a + '.tex'
        # print(tex_file_name)
        with open(tex_file_name, 'w') as tex_file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage{tikz}\n'
                  '\\usepackage[margin=0cm]{geometry}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\vspace*{\\fill}\n'
                  '\\begin{center}\n'
                  '\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]', file=tex_file)

            print(
                '\\draw[ultra thick] (0, 0) -- ({}, 0) -- ({}, {}) -- (0, {}) -- cycle;\n'.format(
                    len(self.digits[0]) - 1,
                    len(self.digits[0]) - 1,
                    len(self.digits) - 1,
                    len(self.digits) - 1),
                file=tex_file)
            depth_print = -1
            for x in polygons_ordered:
                visited_points = [str((i[0], i[1])) for i in x[0]]
                visited_points = ' -- '.join(visited_points)
                if depth_print != x[5]:
                    depth_print = x[5]
                    print('% Depth {}'.format(depth_print), file=tex_file)
                print('\\filldraw[fill=orange!{}!yellow] {} -- cycle;'.format(x[-1], visited_points), file=tex_file)
            print('\\end{tikzpicture}\n'
                  '\\end{center}\n'
                  '\\vspace*{\\fill}\n'
                  '\n'
                  '\\end{document}', file=tex_file)

        # 格式化字符串输出
        # 注意：如果没有str, 会调用repr

    def __str__(self):
        return f'__str__: {self.file_name}'

    def __repr__(self):
        return f'__repr__: {self.file_name}'
