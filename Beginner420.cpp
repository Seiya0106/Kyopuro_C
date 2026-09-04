#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <numbers>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <map>
#include <bitset>
#include <numeric>
using namespace std;
using ll = long long;

int main() 
{
    int n, q;
    cin >> n >> q;
    vector<ll> a(n);
    vector<ll> b(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n; i++){
        cin >> b[i];
    }
    vector<ll> min_num(n);
    for (int i = 0; i < n; i++){
        min_num[i] = min(a[i], b[i]);
    }
    ll total = accumulate(min_num.begin(), min_num.end(), 0ll);
    for (int i = 0; i < q; i++){
        char c;
        int x;
        ll v;
        cin >> c >> x >> v;
        x--;
        if (c == 'A'){
            a[x] = v;
        }
        else{
            b[x] = v;
        }

        // 最小値を更新し、差分をtotalに追加
        total -= min_num[x];
        min_num[x] = min(a[x], b[x]);
        total += min_num[x];

        cout << total << endl;
    }
    return 0;
}
