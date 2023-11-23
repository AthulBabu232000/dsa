# given an array and its length
# return length of maximum subarray with sum = 0
def maxLen(n, arr):
    for i in range(n):
        for j in range(i + 1):
            if sum(arr[j : n - i + j]) == 0:
                print(arr[j : n - i + j])
    return 0


arr = [15, 2, 2, 8, 1, -23, 23]
# n=len(arr)
# result=maxLen(n,arr)
# print(result)
## this code works fine but it has a time complexity of O(n**2)
## which is not acceptible in the higher testcases


# let me try this code that i have implemented with the support of blackbox ai
# blackbox is dumb
# but chatgpt give me this code it is marvelous
def largest_subarray_with_sum_zero(arr):
    n = len(arr)  # length of array
    max_length = 0  #
    cumulative_sum = 0  # sum is add from the beginning
    sum_dict = {0: -1}  # cumilative_sum mapped along with index as value

    for i in range(n):
        cumulative_sum += arr[i]
        if cumulative_sum in sum_dict:
            max_length = max(max_length, i - sum_dict[cumulative_sum])
        if cumulative_sum not in sum_dict:
            sum_dict[cumulative_sum] = i
    print(sum_dict)
    return max_length


arr = [15, -2, 2, -8, 1, 7, 10, 23]
arr = [5, 4, -1, 1]
result = largest_subarray_with_sum_zero(arr)
print(result)
# i wonder how this code really works
# if there is a target_sum other than 0 say it is "k"
# if cumilative_sum - k in sum_dict: i-sum_dict[cumilative_sum-k]
# infact this is something with hashmap in python dictionaries
# which i don't understand on 20th july 2023
# The key insight is that if you encounter the same cumulative sum
#  twice while iterating through the array,
#  it means that the subarray between the two
#  occurrences of that cumulative sum has a sum of zero. 
# This allows you to calculate the length of subarrays
#  with a sum of zero efficiently.
# i understand it on sept 10 night 
