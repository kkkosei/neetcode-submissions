class Solution:

    # ["Hello", "World"] -> "5#Hello5#World"
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        if encodedStr == 0:
            return encodedStr

        for word in strs:
            encodedStr += str(len(word)) + "#" + word

        return encodedStr

    # "5#Hello5#World" -> ["Hello", "World"]
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            count = int(s[i:j])
            strs.append(s[j + 1:j + 1 + count])

            i = j + 1 + count

        return strs
            
            
                

