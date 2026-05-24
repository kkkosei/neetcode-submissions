class Solution:

    # ["Hello", "World"] -> "5#Hello5#World"
    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    # "5#Hello5#World" -> ["Hello", "World"]
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            count = int(s[i:j])
            i = j + 1
            j = count + i

            res.append(s[i:j])

            i = j

        return res
            
            
                

