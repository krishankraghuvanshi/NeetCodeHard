class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)

        best = 0

        stack = []
        for i in range(N):
            cur = i
            while len(stack) and stack[-1][1] > heights[i]:
                k, h = stack.pop()
                best = max(best, (i-k)*h)
                cur = k
            stack.append((cur, heights[i]))
        while len(stack):
            k, h = stack.pop()
            best = max(best, (N-k)*h)
        return best            

        