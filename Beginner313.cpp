#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#include <numbers>
#include <iomanip>
#include <queue>
#include <stack>
#include <algorithm>
#include <map>
using namespace std;
using ll = long long;

int main() 
{
    int n;
    cin >> n;
    vector<ll> a(n);
    ll total = 0;
    for (int i = 0; i < n; i++){
        cin >> a[i];
        total += a[i];
    }

    sort(a.begin(), a.end());
    
    ll avg = total / n;
    ll rem = total % n;
    
    vector<ll> b(n, avg);
    for (int i = n - rem; i < n; i++){
        b[i]++; // 足りない分だけ足す
    }
    
    ll diff_sum = 0;
    for (int i = 0; i < n; i++){
        diff_sum += abs(a[i] - b[i]);
    }

    cout << diff_sum / 2 << endl;
    return 0;
}
