class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            if v in h:
                return [h[v], i]

            h[target - v] = i

            