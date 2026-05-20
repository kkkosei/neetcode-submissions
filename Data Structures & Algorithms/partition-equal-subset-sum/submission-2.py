class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        for num in nums:
            nextDP = set()
            for t in dp:
                nextDP.add(t + num)
                nextDP.add(t)
            dp = nextDP
        
        return sum(nums) // 2 in dp  