class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        r = 0
        seen = []
        max_length = 0

        while r < len(s):

            if s[r] not in seen:
                seen.append(s[r])
                max_length = max(max_length, len(seen))
                r = r + 1

            else:
                seen.remove(s[l])
                l = l + 1

        return max_length