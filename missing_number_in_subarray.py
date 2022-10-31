# Missing number in array
# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4
# Soltion 1:
# Through below code all the test cases are passed however conceptionally this is not the best approach to solve the problem.
# Concept used below is very simple we are given that the array should have - 1 to n intergers but there is one integer which is missing between 1 to n
# so to solve the problem we first created a dictionary which has all the integers present in array and we will iterate through 1 to n and check if the list thats we have 
# formed has the element present in it or not.
class Solution:
    def MissingNumber(self,array,n):
        dict={}
        for i in array:
            dict[i]=1
        keys=dict.keys()
        # print(keys)
        # print(keys)
        for i in range(1,n+1):
            if i not in keys:
                return i
	
# much simpler soluution but doesnt pass all the test case and I am not sure why its not able to pass
class Solution:
    def MissingNumber(self,array,n):
        # dict={}
        # for i in array:
        #     dict[i]=1
        # keys=dict.keys()
        # print(keys)
        for i in range(1,n+1):
            if i not in array:
                return i
# It throw exceed time limit exception

# Solution :2 
# we know sum of all n natural nos. is n(n+1)/2 so we are given that we have 1 no. which is missing from the sum of n natural numbers. So we can find sum of n natural nos.
# and subtract n-1 natural nos. from that sum to get that one missing no.

# All the test cases are passed 
class Solution:
    def MissingNumber(self,array,n):
        sum_n=(n*(n+1))/2
        # print(sum_n)
        for i in array:
            sum_n=sum_n-i
        return int(sum_n)

# Solution :3
# there is a third solution possible for this question which is based on xor property. We know that the xor of two nos. is 0 so since we know that one of the number is missing 
# in the given array so if we xor 1 to n nos. and if we xor the nums present in the array we will get the number which is not present in the array.
# example:
# (1^2^3^5)^(1^2^3^4^5)
# all 1,2,3,5 will become 0 upon xoring except the first number.
class Solution:
    def MissingNumber(self,array,n):
        res=0
        for i in range(1,len(array)+1):
            res=res^array[i-1]
            res=res^i
        res=res^n
        
        return res
