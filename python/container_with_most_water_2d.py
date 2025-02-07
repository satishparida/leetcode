class Solution:
    def maxArea(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while(left <= right):
            area = max(area, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

s = Solution()
s.maxArea([10,1,6,1,1,1,100,100,1,1,1])