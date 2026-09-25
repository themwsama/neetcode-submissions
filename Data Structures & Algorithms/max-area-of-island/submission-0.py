class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum_area = 0
        visited_nodes = set()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) in visited_nodes:
                    continue

                if grid[y][x] == 1:
                    # start BFS
                    stack = []
                    stack.append((y, x))
                    size = 0
                    while stack:
                        node = stack.pop()
                        visited_nodes.add((node[0], node[1]))
                        size += 1

                        up = (max(0, node[0] - 1), node[1])

                        right = (node[0], min(node[1] + 1, len(grid[0])-1))

                        down = (min(len(grid)-1, node[0] + 1), node[1])

                        left = (node[0], max(node[1] - 1, 0))

                        
                        
                        if up not in visited_nodes and grid[up[0]][up[1]] == 1:
                            stack.append(up)
                            visited_nodes.add(up)
                        if down not in visited_nodes and grid[down[0]][down[1]] == 1:
                            stack.append(down)
                            visited_nodes.add(down)
                        if right not in visited_nodes and grid[right[0]][right[1]] == 1:
                            stack.append(right)
                            visited_nodes.add(right)
                        if left not in visited_nodes and grid[left[0]][left[1]] == 1:
                            stack.append(left)
                            visited_nodes.add(left)

                        

                    maximum_area = max(size, maximum_area)


        return maximum_area