class Solution(object):
    def findSpecialInteger(self, arr):
        time = len(arr) // 4 + 1
        count = 1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                count += 1
                if count >= time:
                    return arr[i]
            else:
                count = 1
        return arr[-1]