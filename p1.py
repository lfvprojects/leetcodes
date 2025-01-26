from typing import List

nums = [1,2,3,4]
target = 6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i, number in enumerate(nums):
            print(found)
            complement = target - number
            print(complement)

            if complement in found:
                return [found[complement], i]
            
            found[number] = i

        return print("Nothing here")
    
solution = Solution()

result = solution.twoSum(nums, target)
print(result)