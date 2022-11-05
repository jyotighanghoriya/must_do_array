python code :
class Solution:
    def trappingWater(self, arr,n):
        left=[]
        right=[]
        left.append(0)
        for i in range(1,len(arr)):
            left.append(max(left[i-1],arr[i-1]))
        # print(left)
        right.append(0)
        count=0
        for i in range(len(arr)-1,0,-1):
            right.append(max(right[count],arr[i]))
            count=count+1
        right.reverse()
        # print("right",right)
        out=[]
        for i in range(len(left)):
            if (min(left[i],right[i])-arr[i])<0:
                out.append(0)
            else:
                out.append((min(left[i],right[i])-arr[i]))
        res=0
        for i in out:
            res=res+i
        return res
Logic is very simple:
you are given the boxes that are present now when its raining the rain water will filled between those boxes. Now if the water is getting stored between 
boxes then amount of water stored between boxes will be equal to the max of left height, max of right height and min of maxleft height and maxright height - height of current block

using namespace std;
int findWater(int arr[], int n) 
{ 
    // left[i] contains height of tallest bar to the 
    // left of i'th bar including itself 
    int left[n]; 
  
    // Right [i] contains height of tallest bar to 
    // the right of ith bar including itself 
    int right[n]; 
  
    // Initialize result 
    int water = 0; 
  
    // Fill left array 
    left[0] = arr[0]; 
    for (int i = 1; i < n; i++) 
       left[i] = max(left[i-1], arr[i]); 
  
    // Fill right array 
    right[n-1] = arr[n-1]; 
    for (int i = n-2; i >= 0; i--) 
       right[i] = max(right[i+1], arr[i]); 
  
    // Calculate the accumulated water element by element 
    // consider the amount of water on i'th bar, the 
    // amount of water accumulated on this particular 
    // bar will be equal to min(left[i], right[i]) - arr[i] . 
    for (int i = 0; i < n; i++) 
       water += min(left[i],right[i]) - arr[i]; 
  
    return water; 
} 

#include <bits/stdc++.h>
using namespace std;
int main()
 {
     int t;
     cin>>t;
     while(t--){
         int n;
         cin>>n;
         int a[n];
         for(int i=0; i<n; i++)
            cin>>a[i];
        cout<<findWater(a,n)<<endl;
     }
	
	return 0;
}
