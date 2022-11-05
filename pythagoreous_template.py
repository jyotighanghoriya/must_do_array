# Concept very Simple:
# a*a+b*b=c*c
# all test cases passed
class Solution:

	def checkTriplet(self,arr, n):
    	dict={}
    	count=0
    	for i in arr:
    	    dict[i*i]=0
    	count =0
    	for i in range(0,len(arr)-1):
    	    for j in range(i+1,len(arr)-1):
    	        try:
        	        if (arr[i]*arr[i]+arr[j]*arr[j]) in dict.keys():
        	            return 1
        	    except:
        	        pass
        return 0
