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

int main() 
{
    int n;
    cin >> n;
    map<int, int> m;
    int ans = 1000000;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        if (m.count(a)){
            ans = min(ans, i - m[a] + 1);
        }
        m[a] = i;
    }

    if (ans == 1000000){
        cout << -1 << endl;
    }
    else{
        cout << ans << endl;
    }
}
