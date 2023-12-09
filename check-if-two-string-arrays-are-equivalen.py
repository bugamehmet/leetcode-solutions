# ''.join(dizi) == eşitse True değilse False
def arrayStringsAreEqual(self, word1, word2):
    merge1 = ''.join(word1)
    merge2 = ''.join(word2)
    return merge1 == merge2

# başka bir çözüm
def arrayStringsAreEqual(self, word1, word2):
    b_1 = ''
    b_2 = ''
    for i in word1:
        b_1 += i
    for j in word2:
        b_2 += j
    if b_1 == b_2:
        return True
    else:
        return False