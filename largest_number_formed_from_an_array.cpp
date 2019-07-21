using namespace std;

bool strcompare(string s1, string s2){
    return stoi(s1+s2)>stoi(s2+s1);
}

int main()
 {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    vector<string>v;
	    for(int i=0; i<n; i++){
	        string a;
	        cin>>a;
	        v.push_back(a);
	    }
	    sort(v.begin(),v.end(),strcompare);
	    for(int i=0; i<n; ++i)
	        cout<<v[i];
	    cout<<endl;
	}
	return 0;
}
