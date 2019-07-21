using namespace std;
int main()
 {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0; i<n; ++i)
	        cin>>a[i];

        stack<int>s;        
        int flag=0;
        for(int i=0;i<n;i++){
            if(s.empty()||a[i]>a[s.top()]){
                s.push(i);
            }
            else{
                int end=s.top();
                int start=end;
               while(s.size()>1){
                   s.pop();
               }
               start=s.top();
               s.pop();
               if(start!=end){
                   flag=1;
                   cout<<"("<<start<<" "<<end<<")"<<" ";
               }
               s.push(i);
            }
        }
        if(!s.empty()){
            int end=s.top();
            int start=end;
            while(s.size()>1){
                   s.pop();
               }
            start=s.top();
            if(start!=end){
                flag=1;
                   cout<<"("<<start<<" "<<end<<")";
               }
        }
        if(!flag){
            cout<<"No Profit";
        }
        cout<<endl;
	}
	return 0;
}
