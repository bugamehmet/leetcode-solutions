class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
    # timesort O(n logn)

#İnsertionSort O(n^2)
"""    class Solution(object):
    def maxProduct(self, nums):
        for i in range(len(nums)):
            x = nums[i]
            j = i - 1
            while j >= 0 and x < nums[j]:
                nums[j+1] = nums[j]
                j = j - 1
            nums[j+1] = x
        return (nums[-1] - 1) * (nums[-2] - 1)
"""