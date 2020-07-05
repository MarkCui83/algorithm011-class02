class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #盛水容器，这是第一次写的，这样写太多if是不是不好？
        left_index = 0
        right_index = len(height) - 1
        left = height[left_index]
        right = height[right_index]
        area_max = 0
        while left_index < right_index:
            area =  min(left,right)*(right_index-left_index)
            if area_max < area:
                area_max = area
            if left < right:
                left_index += 1
                left = height[left_index]
                continue
            if left > right:
                right_index -= 1
                right = height[right_index]
                continue
            if left == right:
                left_index += 1
                right_index -= 1
                left = height[left_index]
                right = height[right_index]
                continue
        return area_max