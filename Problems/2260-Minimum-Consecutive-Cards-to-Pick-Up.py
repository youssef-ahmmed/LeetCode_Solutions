class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        last_seen = {}

        for i, card in enumerate(cards):
            if card in last_seen:
                res = min(res, i - last_seen[card] + 1)
            last_seen[card] = i

        return res if res != float("inf") else -1
