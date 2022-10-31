# Missing number in array
# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4

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
