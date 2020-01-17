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

