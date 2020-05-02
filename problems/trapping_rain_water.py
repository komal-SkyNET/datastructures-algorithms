"""
Avg_runtime: 48ms
https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
    
    def trap(self, height: List[int]) -> int:
        index_stack = []
        ans = 0
        for cur in range(len(height)):
            while(len(index_stack)>0 and height[cur] > height[index_stack[-1]]):
                top = index_stack.pop()
                if len(index_stack) != 0:
                    bounded_height = min(height[cur], height[index_stack[-1]]) - height[top]
                    distance = cur - index_stack[-1] - 1
                    ans += distance * bounded_height
            index_stack.append(cur)
        return ans
