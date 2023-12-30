class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # Eğer dizinin uzunluğu 0 ise, hiç şifreleme yapılamaz; bu nedenle 0 döndürülür.
        if n == 0:
            return 0

        # Dinamik programlama tablosu: Belirli bir pozisyondaki şifreleme sayısını saklar
        dp = [0] * (n + 1)
        
        # Başlangıç durumu: İlk rakamdan önce hiç şifreleme yapılmamıştır, bu nedenle 1.
        dp[0] = 1

        # Rakam dizisini tarayarak şifreleme sayısını hesapla
        for i in range(1, n + 1):
            # Eğer mevcut rakam sıfırdan farklı ise, şu anki pozisyon için geçerli olan şifreleme sayısını güncelle.
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Eğer mevcut rakamla bir önceki rakamın oluşturduğu iki haneli sayı 10 ile 26 arasında ise, 
            # bu durumda yeni bir şifreleme yapılabileceği için şifreleme sayısını güncelle.
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        # Son pozisyondaki şifreleme sayısını döndür.
        return dp[n]
