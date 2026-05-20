class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur):
            if len(nums) == i:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            while len(nums) > i+1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, cur)
        dfs(0, [])
        return res


