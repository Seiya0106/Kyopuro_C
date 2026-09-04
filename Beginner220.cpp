#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <numbers>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <numeric>
using namespace std;
using ll = long long;

int main()
{
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    ll x;
    cin >> x;
    ll a_total = accumulate(a.begin(), a.end(), 0ll);
    ll total = 0, ans = 0;
    int idx = 0;
    // 配列の合計から周回分の合計と何項足したかを求める
    total += a_total * (x / a_total);
    ans += n * (x / a_total);
    // ラスト1周で何項足したかを求める
    for (ll val : a){
        total += val;
        ans++;
        if (total > x){
            cout << ans << endl;
            break;
        }
    }
    return 0;
}
