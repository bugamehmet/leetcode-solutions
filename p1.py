# [k:k+3] 3'lü grupamak için

def largestGoodInteger(self):
    liste = []
    for k in range(len(self.num) - 2):
        grup = self.num[k:k+3]
        if( grup[0] == grup[1] and grup[0] == grup[2] and grup[1] == grup[2]):
            liste.append(grup)
    if(len(liste) == 0):
        print("")
    else:
        maxss = str(max(liste))
        print(maxss)