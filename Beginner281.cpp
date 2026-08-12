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
#include <numeric>
using namespace std;
using ll = long long;

int main() 
{
    int n;
    ll t;
    cin >> n >> t;
    vector<ll> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    const ll rem = t % accumulate(a.begin(), a.end(), 0ll);
    ll sum = 0;
    for (int i = 0; i < n; i++){
        if (sum + a[i] > rem){
            cout << i + 1 << " " << rem - sum << endl;
            return 0;
        }
        sum += a[i];
    }
}
