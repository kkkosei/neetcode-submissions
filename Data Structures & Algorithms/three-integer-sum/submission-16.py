class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k in range(0, len(nums) - 2):
            l, r = k + 1, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r]
                target = -nums[k]


                if total == target:
                    if ([nums[k], nums[l], nums[r]]) not in res:
                        res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif total < target:
                    l += 1

                elif total > target:
                    r -= 1

        return res
