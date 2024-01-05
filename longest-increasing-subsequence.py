class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        tail = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, tail)
            dp[i] = num
            if i == tail:
                tail += 1
        return tail
    
"""
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

başlangıçta dp dizisini sıfırlarla doldurup, tail değişkenini 0 yapıyoruz. Ardından, nums dizisinin her bir öğesini şu şekilde işliyoruz:

1 - İkili aramayı (bisect) kullanarak dp dizisinde num'dan daha küçük veya eşit olan en büyük değeri buluyoruz.

2 - Bu değeri, num'un tail'in bir sonraki öğesi olarak ayarlamak için kullanıyoruz.

3 - tail'i, num'un tail'in bir sonraki öğesi olarak ayarlanması gerektiğinden bir arttırıyoruz.

"""