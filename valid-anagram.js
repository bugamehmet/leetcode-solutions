var isAnagram = function(s, t) {
  // Eğer iki dize farklı uzunluktaysa, anagram olamazlar.
  if (s.length !== t.length) return false;

  // 26 elemanlı bir diziyi sıfırlarla doldur.
  const charMap = Array(26).fill(0);

  // Her iki diziyi tarayarak karakter sayılarını güncelle.
  for (let i = 0; i < s.length; i++) {
      // Karakterlerin ASCII değerlerini kullanarak 0'dan başlayan indekslere ekleme veya çıkarma yap.
      charMap[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
      charMap[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
  }

  // charMap dizisindeki her elemanın 0 olup olmadığını kontrol et.
  // Eğer her eleman 0 ise, iki dize anagramdır.
  return charMap.every(count => count === 0);
};
