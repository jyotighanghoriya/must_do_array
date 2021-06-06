# Concept : Here we have to make the decision whether we should add the element to the current calculated sum or to start from the current position
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
# Example 2:

# Input:
# N = 4
# arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)

# Your Task:
# You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and returns the sum of subarray with maximum sum.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,size):
        curr_sum=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
            curr_sum=max(curr_sum+arr[i],arr[i])
            if curr_sum>max_sum:
                max_sum=curr_sum
        return max_sum
