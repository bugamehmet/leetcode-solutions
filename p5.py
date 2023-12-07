# Find Words That Can Be Formed by Characters

words = ["cat","bt","hat","tree"]
chars = "atach"


dizi = []
for j in words:
    dizi.append(j)
print(dizi)

sayac = 0
for k in chars:
    print(k)
    if k in dizi:
        sayac += 1

print(sayac)