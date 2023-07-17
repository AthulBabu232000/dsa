
    def subArraySum(self,arr, n, sum_): 
        A = []
        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > sum_ and start < i-1:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == sum_:
                A.append(start+1)
                A.append(i)
                return A
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        A.append(-1)
        return A