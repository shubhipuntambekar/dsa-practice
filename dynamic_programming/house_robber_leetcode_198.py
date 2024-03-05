"""
    Company Tags: Amazon, OYO Rooms, Paytm, Walmart, Google, Flipkart, LinkedIn, Airbnb
    LeetCode: https://leetcode.com/problems/house-robber/description/
    Difficulty: Medium
    --------------------------------------------------------------------------------------------------------------------
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
    connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
    can rob tonight without alerting the police. (also known as Stickler Thief)
    --------------------------------------------------------------------------------------------------------------------
    Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

    Example 3:
    Input: nums = [2,1,1,2]
    Output: 4
    Explanation: Rob house 1 (money = 2), rob house 4 (money = 2).
    Total amount you can rob = 2 + 2 = 4.
    --------------------------------------------------------------------------------------------------------------------
    Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
    --------------------------------------------------------------------------------------------------------------------
"""


# Approach 1: Using Recursion + Memoization
# Time Complexity:
# Only Recursion: O(2^n)
class RecursiveMemoizationSolution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)
        return self.rob_helper(nums, dp, 0, n)

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
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            steal = nums[i-1] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal, skip)

        return dp[n]
