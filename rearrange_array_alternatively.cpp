using namespace std;

void arrangeAlt(long long int a[], int n){
    int mxin = n-1, mnin = 0;
    long long int mxele = a[n-1]+1;
    if(n==1){
        cout<<a[0];
        return;
    }
    for(int i=0; i<n; i++){
        if(!(i%2)){
            a[i] += a[mxin]%mxele*mxele;
            mxin--;
        }
        else{
            a[i] += a[mnin]%mxele*mxele;
            mnin++;
        }
    }
    for(int i=0; i<n; i++){
        a[i] = a[i]/mxele;   
        cout<<a[i]<<" ";
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
        arrangeAlt(a,n);
        cout<<endl;
    }
	return 0;
}
