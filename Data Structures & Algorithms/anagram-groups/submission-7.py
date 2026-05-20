class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        # hs = {
        #     [0] * 26 : [""]
        # }
        for c in strs:
            key = [0] * 26
            for a in c:
                key[ord(a) - ord("a")] += 1
            hs[tuple(key)].append(c)


        return list(hs.values())
            

         

