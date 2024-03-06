"""
    Company Tags: Airbnb, Microsoft
    LeetCode: https://leetcode.com/problems/house-robber-ii/
    Difficulty: Medium
    --------------------------------------------------------------------------------------------------------------------
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
    one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
    two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
    can rob tonight without alerting the police.
    --------------------------------------------------------------------------------------------------------------------
    Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 3:
    Input: nums = [1,2,3]
    Output: 3
    --------------------------------------------------------------------------------------------------------------------
    Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
    --------------------------------------------------------------------------------------------------------------------
"""


# Approach 1: Using Recursion + Memoization
# Time Complexity:
# Only Recursion: O(2^n)
class RecursiveMemoizationSolution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [-1] * (n + 1)
        steal_zero = self.rob_helper(nums, dp, 0, n-1)

        dp = [-1] * (n + 1)
        skip_zero = self.rob_helper(nums, dp, 1, n)
        return max(steal_zero, skip_zero)

    def rob_helper(self, nums: list, dp: list, i: int, n: int) -> int:
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]

        steal = nums[i] + self.rob_helper(nums, dp, i+2, n)
        skip = self.rob_helper(nums, dp, i+1, n)

        dp[i] = max(steal, skip)
        return dp[i]


# Approach 2: Using Bottom Up Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class BottomUpSolution:

    @staticmethod
    def rob(nums: list) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n):
            steal = nums[i-1] + (dp[i-2] if i-2 >= 0 else 0)
            skip = dp[i-1]
            dp[i] = max(steal, skip)

        steal_zero = dp[n-1]

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            steal = nums[i-1] + (dp[i-2] if i-2 >= 0 else 0)
            skip = dp[i-1]
            dp[i] = max(steal, skip)

        skip_zero = dp[n]

        return max(steal_zero, skip_zero)


# Approach 3: Using Bottom Up Solution without Extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
class BottomUpSolutionNoExtraSpace:

    def rob(self, nums: list) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        steal_zero = self.solve(nums, 0, n-1)
        skip_zero = self.solve(nums, 1, n)

        return max(steal_zero, skip_zero)

    @staticmethod
    def solve(nums: list, l: int, r: int) -> int:
        a, b = 0, 0

        for i in range(l, r):
            steal = nums[i-1] + a
            skip = b
            c = max(steal, skip)
            a, b = b, c

        return b

