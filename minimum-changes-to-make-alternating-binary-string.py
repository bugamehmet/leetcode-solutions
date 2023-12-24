class Solution:
    def minOperations(self, s: str) -> int:
        start_char = "0"
        operations = 0
        for char in s:
            if char == start_char:
                operations += 1
            start_char = "0" if start_char == "1" else "1"
        return min(operations, len(s) - operations)
