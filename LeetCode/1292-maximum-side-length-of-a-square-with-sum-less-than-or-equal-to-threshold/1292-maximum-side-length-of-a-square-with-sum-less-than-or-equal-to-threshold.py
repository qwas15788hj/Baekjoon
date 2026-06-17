class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        
        arr = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + mat[i-1][j-1]

        for size in range(min(n, m), 0, -1):
            for i in range(size, n+1):
                for j in range(size, m+1):
                    if arr[i][j] - arr[i-size][j] - arr[i][j-size] + arr[i-size][j-size] <= threshold:
                        return size
        
        return 0