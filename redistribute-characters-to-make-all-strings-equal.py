from collections import Counter
class Solution:
    
    #bu fonksiyon liste içindeki kelimelerin harf sayılarını analiz eder ve eşit olup olmadığını kontrol eder
    def makeEqual(self, words: List[str]) -> bool:
        # Tüm kelimelerin harflerini birleştirerek bir string oluştur ve her harfin kaç kez geçtiğini sayan bir Counter nesnesi oluştur
        char_count = Counter(''.join(words))
        
        # Tüm karakter sayılarının, kelime sayısına bölünüp bölünmediğini kontrol et
        # Yani, her harfin toplam sayısı, kelimelerin sayısına tam bölünebiliyor mu kontrol ediyoruz.
        # Eğer tüm harf sayıları eşit bir şekilde dağılıyorsa, bu durumda True dönecektir.
        # Aksi takdirde, False dönecektir.
        return all(count % len(words) == 0 for count in char_count.values())
