# Find Words That Can Be Formed by Characters

words = ["cat","bt","hat","tree"]
chars = "atach"
words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"

"""
for kelime in kelimeler: döngüsü ile kelimeler listesindeki her bir kelimeye tek tek erişiliyor.
set(kelime) kullanılarak kelimenin içindeki benzersiz karakterlere erişiliyor. Bu adım, her bir karakterin sayısını sayarken tekrarları önlemeye yardımcı olur.
all(kelime.count(char) <= karakterler.count(char) for char in set(kelime)): ifadesi, kelimenin her karakteri için kontrol ettiği bir şartı içerir. Bu şart, kelimenin her bir karakterinin, karakterler dizesindeki aynı karakterin sayısından küçük veya eşit olup olmadığını kontrol eder.
Eğer bu şart, kelimenin her karakteri için sağlanıyorsa (yani, all fonksiyonu True döndürüyorsa), o zaman bu kelimenin uzunluğu toplam_uzunluk değişkenine eklenir (toplam_uzunluk += len(kelime)).

"""

top = 0
for word in words:
    if all(word.count(char) <= chars.count(char) for char in set(word)):
        top += len(word)
print(top)