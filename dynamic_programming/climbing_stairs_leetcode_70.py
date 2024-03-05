"""
    Company Tags: Google, Amazon, OYO Rooms, Microsoft, Adobe, Flipkart, Siemens
    LeetCode: https://leetcode.com/problems/climbing-stairs/description/
    Difficulty: Easy
    --------------------------------------------------------------------------------------------------------------------
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    --------------------------------------------------------------------------------------------------------------------
    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    --------------------------------------------------------------------------------------------------------------------
    Constraints:
    1 <= n <= 45
    --------------------------------------------------------------------------------------------------------------------
"""


# Approach 1: Using Recursion + Memoization
# Time Complexity:
# Only Recursion: O(2^n)
class RecursiveMemoizationSolution:
    def climb_stairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.solve(n, dp)

    def solve(self, n: int, dp: list) -> int:
        if dp[n] != -1:
            return dp[n]
        elif n < 0:
            return 0
        elif n == 0:
            dp[n] = 1
        else:
            dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)
        return dp[n]


# Approach 2: Using Bottom Up Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class BottomUpSolution:

    @staticmethod
    def climb_stairs(n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Approach 2: Using Bottom Up Solution without Extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
class BottomUpSolutionNoExtraSpace:

    @staticmethod
    def climb_stairs(n: int) -> int:
        if n <= 1:
            return 1

        a, b, c = 1, 1, -1
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c

        return c
