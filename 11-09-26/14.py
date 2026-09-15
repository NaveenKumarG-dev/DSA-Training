class Solution:
    def rearrange(self, arr):
        positive = []
        negative = []

        for i in arr:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)

        length = min(len(positive), len(negative))
        result = []

        for i in range(length):
            result.append(positive[i])
            result.append(negative[i])

        result.extend(positive[length:])
        result.extend(negative[length:])
        
        arr[:] = result