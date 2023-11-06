class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

jewels = "aA"
stones = "aAAbbbb"
c = Solution()
x = c.numJewelsInStones(jewels, stones)
print(x)

# new = set(jewels)
# print(new)
# count =0
# x = (sum(stones.count(i) for i in new))
# print(x)
