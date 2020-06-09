from itertools import permutations 
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[-1]
