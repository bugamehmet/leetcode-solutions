var numSpecial = function(mat) {
  const rows = mat.length;
  const cols = mat[0].length;
  const rowSum = new Array(rows).fill(0);
  const colSum = new Array(cols).fill(0);

  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          rowSum[i] += mat[i][j];
      }
  }
  for (let j = 0; j < cols; j++) {
      for (let i = 0; i < rows; i++) {
          colSum[j] += mat[i][j];
      }
  }
  let result = 0;
  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          if (mat[i][j] === 1 && rowSum[i] === 1 && colSum[j] === 1) {
              result += 1;
          }
      }
  }
  return result;
};

/*
1- const rows = mat.length; ve const cols = mat[0].length;: matrisin satır ve sütun sayısını belirleriz.

2- const rowSum = new Array(rows).fill(0); ve const colSum = new Array(cols).fill(0); : satırların ve sütunların toplamlarını tutacak olan dizileri oluşturduk. 

3- İlk iki iç içe geçmiş döngü, matrisin her elemanının satır toplamlarını hesaplar. İlk döngü, her satırı dolaşır ve her bir elemanın değerini ilgili satırın toplamına ekler.

4- Sonraki iki iç içe geçmiş döngü, matrisin her elemanının sütun toplamlarını hesaplar. İkinci döngü, her sütunu dolaşır ve her bir elemanın değerini ilgili sütunun toplamına ekler.

5- Son döngü, matrisin her elemanını kontrol eder. Eğer eleman 1 ise ve aynı zamanda kendi satırında (rowSum[i] === 1) ve kendi sütununda (colSum[j] === 1) yalnızca bir tane 1 bulunuyorsa, bu bir özel hücredir ve result değişkeni artırılır.

O(m + n)
*/