class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, v in enumerate(nums):
            if v in a:
                return [a[v], i]

            a[target - v] = i

            