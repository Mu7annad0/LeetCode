# 1. Two Sum 
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# https://leetcode.com/problems/two-sum/description/


from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashma = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashma:
                return [hashma[diff], i]
            hashma[n] = i