class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > 0:
            k -= 1
            i = 1
            while i < n:
                nums[0], nums[i] = nums[i], nums[0]
                i += 1
        return nums