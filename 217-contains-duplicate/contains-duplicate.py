from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        x = Counter(nums)
        for value in x.values():
            if value >= 2:
                return True
            
        return False
        

        