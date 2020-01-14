class Solution:
    def trap(self, height):
        def getWater(left, right):
            water_high = min(height[left], height[right])
            total_water = 0
            for i in range(left + 1, right):
                total_water += (water_high - height[i])
            return total_water

        def get_max_index(left, right):
            max_index = left
            for i in range(left, right + 1):
                if height[max_index] < height[i]:
                    max_index = i
            return max_index

        def getTrap(left, right):
            if right - left < 2:
                return 0
            if max(height[left + 1: right]) < min(height[left], height[right]):
                return getWater(left, right)
            else:
                mid = get_max_index(left + 1, right - 1)
                return getTrap(left, mid) + getTrap(mid, right)

        return getTrap(0, len(height) - 1)


if __name__ == '__main__':
    solution = Solution()
    test_case = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(test_case)
    print("result = ", result)
