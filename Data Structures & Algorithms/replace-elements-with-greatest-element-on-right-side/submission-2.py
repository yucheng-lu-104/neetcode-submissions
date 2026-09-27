class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1 # replace the last element with -1

        for i in range(len(arr) - 1, -1, -1): # starting from the last index backward to 0
            # comparing the current right max with the current number
            newMax = max(rightMax, arr[i]) 
            # change the current number with the right max
            arr[i] = rightMax
            # updating the right max with the new max
            rightMax = newMax
        
        return arr