"""
    Company Tags: Amazon, Microsoft, Oyo, SnapDeal, MakeMyTrip, Goldman Sachs, MAQ Software, Adobe
    LeetCode: https://leetcode.com/problems/fibonacci-number/description/
    Difficulty: Easy
    --------------------------------------------------------------------------------------------------------------------
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
    is the sum of the two preceding ones, starting from 0 and 1. That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).
    --------------------------------------------------------------------------------------------------------------------
    Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    --------------------------------------------------------------------------------------------------------------------
    Constraints:
    0 <= n <= 30
    --------------------------------------------------------------------------------------------------------------------
"""


# Approach 1: Using Recursion + Memoization
# Time Complexity:
# Only Recursion: O(2^n)

class RecursiveMemoizationSolution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.solve(n, dp)

    def solve(self, n: int, dp: list) -> int:
        if dp[n] != -1:
            return dp[n]
        elif n <= 1:
            dp[n] = n
        else:
            dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)

        return dp[n]


# Approach 2: Using Bottom Up Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class BottomUpSolution:

    @staticmethod
    def fib(n: int) -> int:
        if n <= 1:
            return n

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Approach 3: Using Bottom Up Solution without Extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
class BottomUpSolutionNoExtraSpace:

    @staticmethod
    def fib(n: int) -> int:
        if n <= 1:
            return n
        a, b, c = 0, 1, -1

        for i in range(2, n + 1):
            c = a + b
            a, b = b, c

        return c
