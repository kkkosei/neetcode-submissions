class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[0] * (n + 1) for _ in range(m + 1)]
        DP[m-1][n-1] = 1



        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                DP[i][j] += DP[i + 1][j] + DP[i][j+1]

        return DP[0][0]
            
