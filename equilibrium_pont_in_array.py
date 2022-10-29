class Solution:
# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Note: Retun the index of Equilibrium point. (1-based index)

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 3 
# Explanation:  
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2). 


# Logic is very simple
# add elements to the left and right in left_sum and right_sum.if left_sum is greater than add elements to right and if right_sum is greater than add elements to the
# right. if only one element than thats the equilibrium point because elements sum to the left and right is zero.
# if at any point sum is becoming same we must check that on adding start+1=end or start=end-1. If this case is satisy then only that point is a equilibrium point.
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        start=0
        end=len(A)-1
        left_sum=0
        right_sum=0
        flag=-1
        left_sum=left_sum+A[start]
        right_sum=right_sum+A[end]
        if len(A)==1:
            return 1
        while start+1<end or start<end-1:
            if left_sum>right_sum:
                # print("leftSum greater",left_sum," ",right_sum," ",start," ",end)
                flag=-1
                end=end-1
                right_sum=right_sum+A[end]
            elif left_sum<right_sum:
                # print("rightSum greater",left_sum," ",right_sum," ",start," ",end)
                flag=-1
                start=start+1
                left_sum=left_sum+A[start]
            else:
                # print(left_sum," ",right_sum," ",start," ",end)
                flag=0
                start=start+1
                end=end-1
                left_sum=left_sum+A[start]
                right_sum=right_sum+A[end]
        if flag==-1 or left_sum !=right_sum:
            return -1
        else:
            return start+1
