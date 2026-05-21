class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        
        for value in strs:

            key = [0] * 26
            for char in value:
                key[ord(char) - ord("a")] += 1
            hs[tuple(key)].append(value)
        
        return list(hs.values())