class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for num in nums:
            nextDp = defaultdict(int)
            for cur_sum, count in dp.items():

                nextDp[cur_sum + num] += count
                nextDp[cur_sum - num] += count
            dp = nextDp

        return dp[target]