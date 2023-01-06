// 1523. Count Odd Numbers in an Interval Range
// Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/


int countOdds(int low, int high) {
        int x = (high - low )/ 2;
        if(((high & 1 )== 0 ) && ((low & 1) == 0)) return x;
        return x + 1;
    }
