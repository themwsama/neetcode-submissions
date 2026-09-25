class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedNodes = set()
        numIslands = 0



        for iy in range(len(grid)):
            for ix in range(len(grid[0])):
                if (iy, ix) in visitedNodes:
                    continue
            
                if grid[iy][ix] == "1":
                    
                    # do bfs until filled whole island
                    start = (iy, ix)
                    stack = []
                    stack.append(start)
                
                    while stack:
                        startPoint = stack.pop()
                        visitedNodes.add(startPoint)

                        rightIndex = min(startPoint[1] + 1, len(grid[0])-1)
                        downIndex = min(startPoint[0] + 1, len(grid)-1)
                        upIndex = max(0, startPoint[0] - 1)
                        leftIndex = max(0,startPoint[1] - 1)

                        right = grid[startPoint[0]][rightIndex]
                        down = grid[downIndex][startPoint[1]]
                        left = grid[startPoint[0]][leftIndex]
                        up = grid[upIndex][startPoint[1]]

                        rightPt = (startPoint[0], rightIndex)
                        downPt = (downIndex, startPoint[1])
                        leftPt = (startPoint[0], leftIndex)
                        upPt = (upIndex, startPoint[1])
                        


                        if right == "1" and rightPt not in visitedNodes:
                            stack.append((startPoint[0], rightIndex))
                        if down == "1" and downPt not in visitedNodes:
                            stack.append((downIndex, startPoint[1]))
                        if left == "1" and leftPt not in visitedNodes:
                            stack.append((startPoint[0], leftIndex))
                        if up == "1" and upPt not in visitedNodes:
                            stack.append((upIndex, startPoint[1]))

                      

                    numIslands += 1

        return numIslands
