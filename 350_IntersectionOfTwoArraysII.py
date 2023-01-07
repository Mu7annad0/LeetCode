# 350. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# #Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=study-plan&id=data-structure-i




from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        # to count the number of values in the list
        # if num1 = [3, 4, 2, 2, 3, 6, 2] 
        # count = {2: 3, 3: 2, 4: 1, 6:1}

        intersection = []
        
        for element in nums2:
            if count[element] > 0:
                # that will ckeck if element in the nums2 there value in nums1 oe not
                intersection.append(element)
                count[element] -= 1
                # to decrese the count of the value in the counter to avoid the redundnt
        return intersection
