import collections as c


class Solution:
    def maxSlidingWindow(self, nums, k):
        deq = c.deque(sorted(nums[:k]))


if __name__ == '__main__':
    k = 3
