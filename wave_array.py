#Method 1: O(n^2)
class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,A,N):
        A.sort()
        temp=0
        for i in range(0,len(A)-1,2):
            temp=A[i]
            A[i]=A[i+1]
            A[i+1]=temp
#Method 2: O(n)
class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,A,N):
        temp=0
        for i in range(0,len(A)-1,2):
            if A[i]<A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp

