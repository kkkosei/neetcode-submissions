class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWord =  min(strs, key=len)
        res = ""


        for i in range(len(minWord)):
            for word in strs:
                
                if minWord[i] != word[i]:
                    return res

            res += minWord[i]
        return res


