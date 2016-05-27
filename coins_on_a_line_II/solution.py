class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # dp[i] means the max value in total from i to end of values
        # dp[i]= max((values[i] + min(dp[i+2],dp[i+3])),(values[i]+values[i+1] + min(dp[i+3],dp[i+4])))
        if not values:
            return False
        size = len(values)
        dp = [0] * size
        dp[size-1] = values[size-1]
        dp[size-2] = values[size-2] + values[size-1]
        for i in range(size - 3, -1, -1):
            if i + 4 <= size - 1:
                a = dp[i + 4]
            else:
                a = 0
            if i + 3 <= size - 1:
                b = dp[i + 3]
            else:
                b = 0
            if i + 2 <= size - 1:
                c = dp[i + 2]
            else:
                c = 0
            dp[i] = max((values[i] + min(b,c)),(values[i]+values[i+1]+min(a,b)))
        sum = 0
        for j in range(size):
            sum += values[j]
        if sum - dp[0] >= dp[0]:
            return False
        return True
