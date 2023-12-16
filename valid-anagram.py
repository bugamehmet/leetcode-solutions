class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Eğer iki dize farklı uzunluktaysa, anagram olamazlar.
        if len(s) != len(t):
            return False
        
        # Karakter sayılarını tutacak sözlükler oluşturuluyor.
        s_count = {}  # İlk dize için karakter sayıları
        t_count = {}  # İkinci dize için karakter sayıları

        # İlk dizeyi tarayarak karakter sayılarını güncelle
        for char in s:
            # get() metodu, belirtilen anahtarın değerini döndürür.
            # Eğer anahtar yoksa, varsayılan olarak 0 değerini döndürür.
            s_count[char] = s_count.get(char, 0) + 1

        # İkinci dizeyi tarayarak karakter sayılarını güncelle
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # İki dizenin karakter sayılarını karşılaştır.
        return s_count == t_count
