class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums): #set = unique elements, if len decreases, dupe is there
            return True
        return False