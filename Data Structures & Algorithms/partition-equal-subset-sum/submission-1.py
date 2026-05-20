class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        def bfs(i, total):
            if total == target:
                return True
            
            if i == len(nums) or total > target:
                return False
            

            return bfs(i + 1, total + nums[i]) or bfs(i + 1, total)


        return bfs(0, 0)

        