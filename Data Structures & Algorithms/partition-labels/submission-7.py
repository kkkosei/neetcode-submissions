class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, v in enumerate(s):
            lastIndex[v] = i

        size = 0
        end = 0
        output = []

        for i, v in enumerate(s):
            size += 1
            if end < lastIndex[v]:
                end = lastIndex[v]

            if i == end:
                output.append(size)
                size = 0
                

                



        return output






            