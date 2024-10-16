from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points) -> int:
        def max_points_from(point_index):
            slopes = defaultdict(int)
            x1, y1 = points[point_index]
            for j in range(len(points)):
                if j == point_index:
                    continue
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                # Normalize the slope
                if dx == 0:  # vertical line
                    slope = ('inf', 0)
                elif dy == 0:  # horizontal line
                    slope = (0, 'inf')
                else:
                    if dy < 0:
                        dx, dy = -dx, -dy  # Normalize direction
                    common_gcd = gcd(dy, dx)
                    slope = (dy // common_gcd, dx // common_gcd)
                
                slopes[slope] += 1
            
            # The maximum count for the same slope + 1 for the current point
            return max(slopes.values(), default=0) + 1

        max_points = 0
        for i in range(len(points)):
            max_points = max(max_points, max_points_from(i))

        return max_points

# Example usage
solution = Solution()
print(solution.maxPoints([[1,1],[2,2],[3,3]]))  # Output: 3
print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # Output: 4
