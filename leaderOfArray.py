# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
# Example 1:

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        out=[]
        out.append(A[N-1])
        for i in range(len(A)-2,-1,-1):
            if out[0]<=A[i]:
                out.insert(0,A[i])
        return out
      
# ----------------------------------------------------------Better Solution down --------------------- All test cases are passed ------------------------------------
# insert takes more time as compared to append because there we are not maintaining indexes.
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        large = 0

        result = []

        for i in range(N-1, -1, -1):

            if A[i] >= large:

                result.append(A[i])

                large = A[i]

        return result[::-1]
