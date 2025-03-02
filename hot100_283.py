class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        slow = fast = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
