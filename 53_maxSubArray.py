
# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# https://leetcode.com/problems/maximum-subarray/description/


def maxSubArray(self, nums):
        max_sub = nums[0]
        cur_sub = 0

        for n in nums:
            if cur_sub < 0:
                cur_sub = 0
            cur_sub += n
            max_sub = max(max_sub, cur_sub)
        return max_sub
      
