def largest_subarray_with_sum_zero(arr):
    n = len(arr)
    max_length = 0
    cumulative_sum = 0
    sum_dict = {0: -1} 

    for i in range(n):
        cumulative_sum += arr[i]
        if cumulative_sum in sum_dict:
            max_length = max(max_length, i - sum_dict[cumulative_sum])
        if cumulative_sum not in sum_dict:
            sum_dict[cumulative_sum] = i
    print(sum_dict)
    return max_length

arr = [15, -2, 2, -8, 1, 7, 10, 23]
result = largest_subarray_with_sum_zero(arr)
print(result)  