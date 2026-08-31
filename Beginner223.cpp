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
    cin >> n;
    vector<double> a(n);
    vector<double> b(n);
    double t = 0;
    for (int i = 0; i < n; i++){
        cin >> a[i] >> b[i];
        t += a[i] / b[i];
    }
    t /= 2;
    double ans = 0;
    for (int i = 0; i < n; i++){
        ans += min(a[i], t * b[i]);
        t -= min(a[i] / b[i], t);
    }

    cout << ans << endl;
    return 0;
}
