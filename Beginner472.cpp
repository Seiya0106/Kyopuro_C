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
    int n, m;
    ll k;
    cin >> n >> m >> k;
    ll total = 0;
    int eat_day = 0;
    vector<ll> a(n);
    vector<bool> isEated(n, false);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n; i++){
        if (i-m >= 0 && isEated[i-m]){
            total -= a[i-m];
            eat_day--;
        }

        if (total + a[i] <= k && eat_day < m){
            cout << "Yes" << endl;
            total += a[i];
            eat_day++;
            isEated[i] = true;
        }
        else{
            cout << "No" << endl;
        }
    }

    return 0;
}
