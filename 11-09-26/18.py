class Solution:
    def rearrange(self, arr):
        arr.sort()

        left = 0
        right = len(arr) - 1

        result = []

        while left < right:
            result.extend([arr[right], arr[left]])
            right -= 1
            left += 1

        if left == right:
            result.append(arr[left])

        arr[:] = result