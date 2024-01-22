class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1
        
        tekrar = 0
        eksik = 0

        for i in range(1, n + 1):
            if count[i] == 0:
                eksik = i
            elif count[i] == 2:
                tekrar = i
        
        return [tekrar, eksik]
