class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_decrease = []  #stack
        i = 0
        water_sum = 0
        while(i < len(height)):
            while(left_decrease and height[i] > height[left_decrease[-1]]):
                stack_top = left_decrease.pop()
                if not left_decrease:   #empty?
                    break               
                bounded_height = min(height[i], height[left_decrease[-1]]) - height[stack_top]
                width = i - left_decrease[-1] - 1
                water_sum += bounded_height * width
            left_decrease.append(i)
            i += 1
        return water_sum