class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        result = 0
        stack = []
        left_bound = [-1] * n
        right_bound = [n] * n

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                right_bound[stack.pop()] = i
            left_bound[i] = stack[-1] if stack else -1
            stack.append(i)

        for i in range(n):
            result += arr[i] * (i - left_bound[i]) * (right_bound[i] - i) % MOD
            result %= MOD

        return result
