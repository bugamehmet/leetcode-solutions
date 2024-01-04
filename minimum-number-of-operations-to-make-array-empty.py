class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        sayilar = {}
        for i in range(n):
            if nums[i] in sayilar:
                sayilar[nums[i]] += 1
            else:
                sayilar[nums[i]] = 1
        toplamAdim = 0
        for sayi in sayilar.values():
            if sayi == 1:
                return -1
            toplamAdim += sayi // 3
            if sayi % 3:
                toplamAdim += 1
        return toplamAdim