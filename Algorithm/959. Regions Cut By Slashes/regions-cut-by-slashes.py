"""
Problem
Regions Cut By Slashes
(https://leetcode.com/problems/regions-cut-by-slashes)

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.
"""
import unittest


class Solution:
    """ Notes:
    Brute force graph
    Be aware: BE very careful when use return in loop 
    When generating hash key, use delimit to avoid collision 
    """
    def regionsBySlashes(self, grid) -> int:
        visited = {}
        new_grid = []
        for i, line in enumerate(grid):
            row = []
            for j, token in enumerate(line):
                if token == ' ':
                    row.append([(i, j, 'whole')])
                elif token == '/':
                    row.append([(i, j, 'leftup'), (i, j, 'rightdown')])
                elif token == '\\':
                    row.append([(i, j, 'leftdown'), (i, j, 'rightup')])
            new_grid.append(row)

        def gen_key(node):
            # generate
            x = node[0]
            y = node[1]
            flag = node[2]
            key = ':'.join([str(x),str(y),flag])
            return key


        def get_valid_node(x, y, direction):
            if x >=0 and x < len(new_grid) and y >=0 and y < len(new_grid):
                for n in new_grid[x][y]:
                    key =  gen_key(n)
                    if key in visited:
                        # !!! It is wrong to use return here, because it's in a loop 
                        continue

                    if n[2] == 'whole':
                        return n
                    if n[2] == 'leftup' and (direction == 'right' or direction == 'down'):
                        return n
                    if n[2] == 'leftdown' and (direction == 'right' or direction == 'up'):
                        return n
                    if n[2] == 'rightup' and (direction == 'left' or direction == 'down'):
                        return n
                    if n[2] == 'rightdown' and (direction == 'left' or direction == 'up'):
                        return n 
            return None


        def visit(node):
            if not node:
                return

            # node = (x, y, 'mark')
            key = gen_key(node)
            visited[key] = True
            x = node[0]
            y = node[1]
            flag = node[2]
            if flag == 'leftup':  # could only go left up
                visit(get_valid_node(x, y - 1, 'left'))
                visit(get_valid_node(x - 1, y, 'up'))
            elif flag == 'leftdown':
                visit(get_valid_node(x, y - 1, 'left'))
                visit(get_valid_node(x + 1, y, 'down'))
            elif flag == 'rightup':
                visit(get_valid_node(x, y + 1, 'right'))
                visit(get_valid_node(x - 1, y, 'up'))
            elif flag == 'rightdown':
                visit(get_valid_node(x, y + 1, 'right'))
                visit(get_valid_node(x + 1, y, 'down'))
            elif flag == 'whole':
                visit(get_valid_node(x, y - 1, 'left'))
                visit(get_valid_node(x - 1, y, 'up'))
                visit(get_valid_node(x, y + 1, 'right'))
                visit(get_valid_node(x + 1, y, 'down'))
                
            else:
                raise

        count = 0
        for row in new_grid:
            for col in row:
                for node in col:
                    key = gen_key(node)
                    if key not in visited:
                        visit(node)
                        count += 1
        return count 


class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        r = s.regionsBySlashes(["//", " /"])
        print(r)
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()