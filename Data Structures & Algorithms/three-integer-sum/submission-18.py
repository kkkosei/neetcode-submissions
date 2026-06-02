class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k in range(len(nums) - 2):
            l, r = k + 1, len(nums) - 1
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while l < r:
                total = nums[l] + nums[r]
                target = -nums[k]


                if total == target:
                    res.append((nums[k], nums[l], nums[r]))
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < target:
                    l += 1

                elif total > target:
                    r -= 1

        return res
