class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        real_k = k % n
        nums.reverse()
        B = int(real_k/2)
        C = int((n - real_k)/2)
        B_start = 0
        B_end = real_k - 1
        C_start = real_k
        C_end = n - 1
        while B > 0:
            nums[B_start], nums[B_end] = nums[B_end], nums[B_start]
            B -= 1
            B_start += 1
            B_end -= 1
        while C > 0:
            nums[C_start], nums[C_end] = nums[C_end], nums[C_start]
            C -= 1
            C_start += 1
            C_end -= 1
        