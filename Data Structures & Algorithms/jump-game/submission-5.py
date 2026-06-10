class Solution:
    def canJump(self, nums: List[int]) -> bool: 

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            jumpLength = nums[i]

            while jumpLength > 0:
                if dfs(i + jumpLength):
                    return True    
                
                jumpLength -= 1


            return False

        return dfs(0)
