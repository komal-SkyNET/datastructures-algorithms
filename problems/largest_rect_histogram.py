"""
Avg_Runtime: 108ms
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        index = 0
        max_area = 0
        while index < len(heights):
            if (not stack) or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index+=1
            else:
                stack_top = stack.pop()
                area = heights[stack_top] * ((index - stack[-1] -1) if stack else index)
                max_area = max(area, max_area)
        return max_area 

"""
Avg_Runtime: 112ms

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for i_current in range(len(heights)):
            if len(stack) == 0:
                stack.append((i_current, heights[i_current]))
            else:
                i_top, h_top = stack[-1]
                if heights[i_current] > h_top:
                    stack.append((i_current, heights[i_current]))
                else:
                    while(len(stack) > 0 and stack[-1][1] > heights[i_current]):
                        i_top, h_top = stack.pop()
                        area_here = (i_current - i_top) * h_top
                        if area_here > max_area:
                            max_area = area_here
                    if heights[i_current] > h_top:
                        stack.append((i_current, heights[i_current]))
                    else:
                        stack.append((i_top, heights[i_current]))
        return max_area
"""
