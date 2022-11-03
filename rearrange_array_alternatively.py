# Rearrange array alternatively:
# concept is very simple: keep two pointers and keep and auxilary array until small<=large. All test cases are passes in below code. Better solution check on gfg.

#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        aux_array=[]
        i=0
        j=len(arr)-1
        count=0
        while i<=j:
            aux_array.append(arr[j])
            j=j-1
            aux_array.append(arr[i])
            i=i+1
            if i==j:
                aux_array.append(arr[i])
            # print(aux_array)
        for i in range(0,len(arr)):
            if len(aux_array)==0:
                pass
            else:
                arr[i]=aux_array[i]
# using namespace std;
# void arrangeAlt(long long int a[], int n){
#     int mxin = n-1, mnin = 0;
#     long long int mxele = a[n-1]+1;
#     if(n==1){
#         cout<<a[0];
#         return;
#     }
#     for(int i=0; i<n; i++){
#         if(!(i%2)){
#             a[i] += a[mxin]%mxele*mxele;
#             mxin--;
#         }
#         else{
#             a[i] += a[mnin]%mxele*mxele;
#             mnin++;
#         }
#     }
#     for(int i=0; i<n; i++){
#         a[i] = a[i]/mxele;   
#         cout<<a[i]<<" ";
#     }
# }

# int main()
#  {
#     int t;
#     cin>>t;
#     while(t--){
#         int n;
#         cin>>n;
#         long long int a[n];
#         for(int i=0; i<n; i++)
#             cin>>a[i];
#         arrangeAlt(a,n);
#         cout<<endl;
#     }
# 	return 0;
# }
