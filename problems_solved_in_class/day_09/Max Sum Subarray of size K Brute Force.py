class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        cur_max = 0
        for i in range(len(arr)-k):
            cur_sum = sum(arr[i:k])
            cur_max = max(cur_sum,cur_max)
            
        return cur_max

sol = Solution()

print(sol.maxSubarraySum([100, 200, 300, 400],2))