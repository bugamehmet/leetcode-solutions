

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        max_player = max(max(matches, key=lambda x: max(x)))
        winners = set()
        losers = defaultdict(int)
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        zero_loss = sorted(winners - set(losers))
        one_loss = sorted({player for player, loss_count in losers.items() if loss_count == 1})
        return [zero_loss, one_loss]