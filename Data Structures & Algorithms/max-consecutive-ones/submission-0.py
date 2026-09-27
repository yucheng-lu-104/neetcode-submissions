class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        current_sum = 0
        greatest_number = 0

        for i in range(len(nums)+1):
            if (i == len(nums)) or (nums[i] == 0):
                if current_sum > greatest_number:
                    greatest_number = current_sum
                current_sum = 0
                i += 1
            
            elif nums[i] == 1:
                current_sum += 1
                i += 1

        return greatest_number