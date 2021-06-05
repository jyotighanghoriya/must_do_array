# Row with max 1s 
# Medium Accuracy: 42.51% Submissions: 35894 Points: 4
# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

# Example 1:

# Input: 
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based
# indexing).

# Example 2:

# Input: 
# N = 2, M = 2
# Arr[][] = {{0, 0}, {1, 1}}
# Output: 1
# Explanation: Row 1 contains 2 1's (0-based
# indexing).

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		max_row=0
		max_sum=0
		row_sum=0
		for i in range(0,n):
		  #  print(arr[i])
		    for j in arr[i]:
		        row_sum=row_sum+j
		      #  print(row_sum)
		    if row_sum>max_sum:
		        max_sum=row_sum
		        max_row=i
		    row_sum=0
		if max_sum ==0 :
		    return -1
		else:
		    return max_row
