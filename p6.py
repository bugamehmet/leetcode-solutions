# Largest Odd Number in String

# for i in range(len(num) - 1, -1, -1): : Bu döngü, num dizisinin sonundan başlayarak başa doğru ilerler. Bu sayede en büyük tek sayıyı bulmak için sondan başlayarak kontrol yapılır.
# if int(num[i]) % 2 == 1: : Her bir karakterin sayısal değeri alınır (int(num[i])) ve bu sayının tek olup olmadığı kontrol edilir (% 2 == 1).
# return num[:i + 1] : Eğer bulunan karakterin sayısal değeri tekse, o karakter ve onun solundaki diğer karakterleri içeren alt dize (num[:i + 1]) fonksiyon tarafından hemen döndürülür. Bu alt dize, baştan itibaren en büyük tek sayıyı temsil eder.

class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ''