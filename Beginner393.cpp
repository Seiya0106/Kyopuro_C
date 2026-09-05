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
    int n, m;
    cin >> n >> m;
    set<pair<int, int>> p;
    int ans = 0;
    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        if (u == v){
            ans++;
        }
        else{
            if (p.count({u, v})){
                ans++;
            }
            else{
                p.insert({u, v});
                p.insert({v, u});
            }
        }
    }

    cout << ans << endl;
    return 0;
}
