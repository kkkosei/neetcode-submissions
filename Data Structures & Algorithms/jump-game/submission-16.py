#DP version
class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        dp = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in dp:
                return dp[i]


            jumpLength = nums[i]

            while jumpLength > 0:
                if dfs(i + jumpLength):
                    dp[i] = True
                    return True    
                
                jumpLength -= 1

            dp[i] = False
            return False

        return dfs(0)
