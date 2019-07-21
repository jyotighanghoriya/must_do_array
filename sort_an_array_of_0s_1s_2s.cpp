using namespace std;

void seggregate(int a[], int n){
    //0 0 0 1 2 2
    //      l
    //        m
    //      h
    int l=0,h=n-1,m=0;
    while(m<=h){
        switch(a[m]){
            case 0: swap(a[l++],a[m++]);
                    break;
            case 1: m++;
                    break;
            case 2: swap(a[m],a[h--]);
                    break;
        }
    }
    for(int i=0; i<n; i++)
        cout<<a[i]<<" ";
}

int main()
 {
	//code
	int t;
	cin>>t;
	
	while(t--){
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0; i<n; i++){
	        cin>>a[i];
	    }
	    seggregate(a,n);
	    cout<<endl;
	}
	return 0;
}
