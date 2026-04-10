class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for values in nums: 
            if values in my_set:
                return True 
            else: 
                my_set.add(values)
                continue
        return False