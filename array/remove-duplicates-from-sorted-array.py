class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        counter = 0
        for i in range(len(nums) - 1):
            if nums[i - counter] == nums[(i + 1) - counter]:
                nums.pop(i - counter)
                counter += 1

        return len(nums)