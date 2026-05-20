class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if a[i] == a[j]:
                    return True
        
        return False