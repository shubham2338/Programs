#User function Template for python3
import bisect
class Solution:
    def constructLowerArray(self,nums, n):
        s = []
        for i in range(n - 1, -1, -1):
            c= bisect.bisect_left(s, nums[i])
            bisect.insort(s, nums[i])
            nums[i] = c
        return nums
