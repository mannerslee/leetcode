class Solution:
    def get_init_index(self, ls):
        if len(ls) == 1:
            return 0
        elif len(ls) == 2:
            if ls[0] <= ls[1]:
                return 0
            else:
                return 1
        else:
            for i in range(len(ls) - 1):
                if ls[i] > ls[i + 1]:
                    return i + 1
            return 0

    def binary_search(self, arr, key):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if key == arr[mid]:
                return mid
            elif key > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1

        init_index = self.get_init_index(nums)
        if target > nums[len(nums) - 1]:
            return self.binary_search(nums[:init_index], target)
        elif target < nums[len(nums) - 1]:
            index = self.binary_search(nums[init_index:], target)
            if index != -1:
                return index + init_index
            else:
                return -1
        else:
            return len(nums) - 1