# Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

# Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

# Example 1:

# Input:
# A[] = {1, 4, 45, 6, 0, 19}
# x  =  51
# Output: 3
# Explanation:
# Minimum length subarray is 
# {4, 45, 6}

# Example 2:
# Input:
# A[] = {1, 10, 5, 2, 7}
#    x  = 9
# Output: 1
# Explanation:
# Minimum length subarray is {10}
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function sb() which takes the array A[], its size N and an integer X as inputs and returns the required ouput.
class Solution:
    def sb(self, arr, n, x):
        temp=[]
        current_sum=0
        initial=0
        temp=[]
        min_array=0
        for i in arr:
            current_sum=current_sum+i
            temp.append(i)
            while current_sum>x:
                if min_array>len(temp):
                    min_array=len(temp)
                elif min_array==0:
                    min_array=len(temp)
                current_sum=current_sum-arr[initial]
                temp.remove(arr[initial])
                initial=initial+1
        return min_array
