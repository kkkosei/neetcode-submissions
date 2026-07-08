class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            #newInterval[1] < interval[0] -> newInterval + intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #interval[1] < newInterval[0] -> res.append(interval)
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # else -> newInterval[min, max]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)

        return res

             

