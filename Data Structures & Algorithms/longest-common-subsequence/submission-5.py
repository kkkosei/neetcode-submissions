class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        # DP = [[0] * (col + 1) for _ in range(row + 1)]
        DP = [0] * (col + 1)

        for i in range(row-1, -1, -1):
            newDP = [0] * (col + 1)
            for j in range(col-1, -1, -1):
                if text1[i] == text2[j]:
                    newDP[j] = DP[j+1] + 1
                else:
                    newDP[j] = max(DP[j], newDP[j+1])
                
            DP = newDP
        

        return DP[0]