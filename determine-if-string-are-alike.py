class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set("aeiouAEIOU")

        # Fonksiyon yerine doğrudan küme işlemleri kullanılıyor
        count_a = sum(1 for char in s[:n//2] if char in vowels)
        count_b = sum(1 for char in s[n//2:] if char in vowels)

        # Karşılaştırma işlemi
        return count_a == count_b