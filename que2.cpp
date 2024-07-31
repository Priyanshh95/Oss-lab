#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n;
    cin>>n;
    vector<double> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    double sum = 0;
    for(auto c : a) sum += c;

    cout<<(sum/n)<<endl;
}