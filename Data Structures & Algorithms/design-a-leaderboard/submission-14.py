class Leaderboard:

    def __init__(self):
        self.cache = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.cache[playerId] = self.cache.get(playerId, 0) + score

    def top(self, K: int) -> int:
        sorted_score = sorted(list(self.cache.values()), reverse=True)
        top_sum = 0
        for i in range(K):
            top_sum += sorted_score[i]

        return top_sum


    def reset(self, playerId: int) -> None:
        self.cache.pop(playerId)

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
