class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #盛水容器，这是读了其他人的代码后，改进了的，效率提高了一点
        left_index = 0
        right_index = len(height) - 1
        area_max = 0
        while left_index < right_index:
            b = right_index - left_index            
            if height[left_index] < height[right_index]:
                h = height[left_index]
                left_index += 1                
            else:
                h = height[right_index]
                right_index -= 1
            area = b * h
            if area_max < area:
                area_max = area
        return area_max