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
    ll k;
    cin >> n >> k;
    set<ll> a;
    for (int i = 0; i < n; i++){
        ll s;
        cin >> s;
        a.insert(s);
    }
    ll total =  k * (k+1) / 2;
    for (auto& b : a){
        if (b <= k){
            total -= b;
        }
    }

    cout << total << endl;
    return 0;
}
