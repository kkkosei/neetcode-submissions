class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in dp:
                return dp[i]
        
            res = float('inf')

            for jumpLength in range(1, nums[i] + 1):
                res = min(res, 1 + dfs(i + jumpLength))
            dp[i] = res

            return res

        return dfs(0)