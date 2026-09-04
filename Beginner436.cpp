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
    ll n, m;
    cin >> n >> m;
    set<pair<ll, ll>> st;
    int ans = 0;
    for (int i = 0; i < m; i++){
        ll r, c;
        cin >> r >> c;
        bool ok = true;
        for (int x = r-1; x <= r+1; x++){
            for (int y = c-1; y <= c+1; y++){
                if (st.count({x, y})){
                    ok = false;
                }
            }
        }
        if (ok){
            st.insert({r, c});
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}
