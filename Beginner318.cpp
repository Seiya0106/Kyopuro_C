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
    int n, d;
    ll p;
    cin >> n >> d >> p;
    vector<ll> f(n);
    for (int i = 0; i < n; i++){
        cin >> f[i];
    }
    sort(f.begin(), f.end(), greater<ll>());

    int count = 0;
    ll total = 0;
    bool isUsed = true;
    ll ans = 0;
    for (int i = 0; i < n; i++){
        if (isUsed){
            count++;
            total += f[i];
        }
        else{
            ans += f[i];
            continue;
        }
        
        if (count == d && total > p){
            ans += p;
            count = 0;
            total = 0;
        }
        else if (count == d){
            ans += total;
            count = 0;
            total = 0;
            isUsed = false;
        }
    }

    cout << ans + min(p, total) << endl;
    return 0;
}
