class Solution:
    def rotateArr(self, arr, d):
        
        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        n = len(arr)
        k = d % n

        reverse(0, k - 1)
        reverse(k, n - 1)
        reverse(0, n - 1)