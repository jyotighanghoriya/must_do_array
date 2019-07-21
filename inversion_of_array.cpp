using namespace std;
long long int inversions=0;
void merge(long long int arr[],int left,int m,int right)
{
    long long int larray[m-left+1],rarray[right-m],i=0,j=0,k=left;
    for(int i=0;i<m-left+1;i++)
        larray[i] = arr[left+i];
    for(int i=0;i<=right-m;i++)
        rarray[i] = arr[m+i+1];
    while(i < m-left+1 && j < right-m)
    {
        if(larray[i] <= rarray[j])
            arr[k++] = larray[i++];
        else
        {
            inversions+=m-left+1-i;
            arr[k++] = rarray[j++];
        }
    }
    while(i < m-left+1)
    {
        arr[k++] = larray[i++];
    }
    while(j < right-m)
    {
        arr[k++] = rarray[j++];
    }
}
void noOfInversions(long long int arr[],int left,int right)
{
    if(left < right)
    {
        int m = (left+right)/2;
        noOfInversions(arr,left,m);
        noOfInversions(arr,m+1,right);
        merge(arr,left,m,right);
    }
}
int main()
 {
	int t;
	cin>>t;
	
	while(t--){
	    int n;
	    cin>>n;
	    long long int a[n];
	    for(int i=0; i<n; i++)
	        cin>>a[i];
	   noOfInversions(a,0,n-1);
	   cout<<inversions<<endl;
	   inversions = 0;
	}
	return 0;
}
