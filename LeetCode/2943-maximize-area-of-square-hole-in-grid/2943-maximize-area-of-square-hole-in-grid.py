class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        max_x = 0
        x = 0
        for i in range(len(hBars)-1):
            if hBars[i]+1 == hBars[i+1]:
                x += 1
                max_x = max(max_x, x)
            else:
                x = 0
        
        max_y = 0
        y = 0
        for i in range(len(vBars)-1):
            if vBars[i]+1 == vBars[i+1]:
                y += 1
                max_y = max(max_y, y)
            else:
                y = 0
        
        return (2+min(max_x, max_y))**2