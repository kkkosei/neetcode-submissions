class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False

            jumpLength = nums[i]

            while jumpLength > 0:
                if dfs(i + jumpLength):
                    dp[i] = True
                    return True
                
                jumpLength -= 1

            dp[i] = False
            return False

        return dfs(0)
                
