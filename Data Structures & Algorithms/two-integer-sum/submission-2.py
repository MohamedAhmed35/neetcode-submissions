class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_idx:
                return [num_idx[diff], i]
            num_idx[n] = i
        
        return 
            