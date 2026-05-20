class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}   # 各文字が最後に現れた index を記録
        l = 0       # window の左端
        res = 0     # 最大長

        for r, char in enumerate(s):
            if char in used and used[char] >= l:
                l = used[char] + 1  # 重複が出たので、左端を更新する

            used[char] = r          # char が現れた最新位置を更新
            res = max(res, r - l + 1)

        return res
