class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Uzunluğa göre sıkıştırma işlemi yapacak olan lambda fonksiyonu
        getLength = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4

        # Önbellek (cache) kullanarak, tekrarlanan hesaplamaları saklamak için kullanılan fonksiyon
        def recur(i, k):
            # Dizinin sonuna ulaştıysak, sıkıştırma işlemi sona erdi, uzunluğu 0 olarak döndür
            if i < 0: return 0

            # Kısıtlı sayıda silme işlemi (k) yapılabileceği için bir rekürsif fonksiyon kullanılır.
            # İlk olarak, s[i] karakterini kaldırmadan devam edilen durumu kontrol et.
            res = recur(i - 1, k - 1) if k else 9e9
            
            # Karakterin tekrar sayısını bulmak ve ardından bu karakterleri sırayla kaldırarak uzunluğu güncellemek.
            freq = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]: 
                    freq += 1
                elif k == 0: 
                    return res
                else: 
                    k -= 1
                res = min(res, recur(j - 1, k) + getLength(freq))
            
            return res
        
        # Dizinin tamamını kapsayan başlangıç durumu ile rekürsif fonksiyonu başlat
        return recur(len(s) - 1, k)
