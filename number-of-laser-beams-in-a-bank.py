class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        const = 0
        tekrar = 0
        for i in range(len(bank)):
            deger = bank[i].count('1')
            const += tekrar * deger
            if deger > 0:
                tekrar = deger
        return const