class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        dp_s = [0] * 26
        dp_t = [0] * 26
        for char_s, char_t in zip(s, t):
            dp_s[ord(char_s) - ord('a')] += 1
            dp_t[ord(char_t) - ord('a')] += 1
        replace_steps = sum(dp_s[i] - dp_t[i] for i in range(26) if dp_s[i] > dp_t[i])

        return replace_steps