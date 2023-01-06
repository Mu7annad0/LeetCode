def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashma = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashma:
                return [hashma[diff], i]
            hashma[n] = i