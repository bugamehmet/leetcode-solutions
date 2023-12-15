class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        tum_sehirler = set() # Küme oluşturmak için A = [1,2,3,4,4,4,5,5,6]   küme = set(A) print(A)  --> 1,2,3,4,5,6 
        gidilen = set()

        for sehir in paths:
            tum_sehirler.add(sehir[0])
            tum_sehirler.add(sehir[1])

        for path in paths:
            gidilen.add(path[1])

        for sehir in tum_sehirler:
            if sehir not in gidilen: # sehir degişkeni gidilen de bulunmuyorsa if bloğu çalışır
                return sehir
            