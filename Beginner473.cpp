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
    int n, k;
    cin >> n >> k;
    map<int, int> num;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        num[a]++;
    }

    int max_num = 0;
    for(auto& [k, v] : num){
        max_num = max(max_num, v);
    }
    int ans = 0;
    for(auto& [k, v] : num){
        if (v >= max_num-1){
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}
