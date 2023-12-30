class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        # Hedef skoru elde etmek için kullanılacak olan dinamik programlama tablosu
        dp = [0] * (target + 1)
        
        # Başlangıç durumu: 0 skor için bir kombinasyon (hiç zar atılmamış durum)
        dp[0] = 1
        
        # Zar atma işleminin her bir adımını simüle etme
        for i in range(1, n + 1):
            # Yeni bir dinamik programlama tablosu oluşturulur
            new_dp = [0] * (target + 1)
            
            # Her bir skor için olasılıkları hesaplama
            for j in range(1, target + 1):
                for x in range(1, min(k, j) + 1):
                    # Zarın değeri kadar geri gidilerek elde edilebilecek kombinasyonlar ekleme
                    new_dp[j] = (new_dp[j] + dp[j - x]) % MOD
            
            # Yeni tablo, bir sonraki zar atma adımında kullanılmak üzere eski tabloya atanır
            dp = new_dp

        return dp[target]