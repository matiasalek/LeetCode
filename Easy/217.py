from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums:
            if i in my_dict and my_dict[i] >= 1:
                return True
            my_dict[i] = my_dict.get(i, 0) + 1
        return False