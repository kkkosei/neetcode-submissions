class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,8,48]
        #[48,48,24,6]
        res = [0] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res

        

       