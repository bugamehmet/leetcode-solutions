class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_zeros_ones_sum = 0

        for i in range(n - 1):
            left_zeros = s[:i + 1].count('0')
            right_ones = s[i + 1:].count('1')

            current_sum = left_zeros + right_ones
            max_zeros_ones_sum = max(max_zeros_ones_sum, current_sum)

        return max_zeros_ones_sum