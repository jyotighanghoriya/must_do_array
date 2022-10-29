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
      
      
