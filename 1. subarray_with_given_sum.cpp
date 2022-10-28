#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        sum=arr[0]
        start=0
        for i in range(1,n+1):
            # print(i)
        
            while(sum>s and start<i-1):
                sum=sum-arr[start]
                start=start+1
                print("start=",start,sum)
            if sum==s:
                print("equal condition encountered",start+1,i)
                return start+1,i
            elif sum<s and i!=n:
                print(i)
                sum=sum+arr[i]
                print("sum=",sum)
        if start<=n:
            return [-1]
