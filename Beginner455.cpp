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
    int n, k;
    cin >> n >> k;
    map<long long, long long> mp;
    vector<long long> value;
    for (int i = 0; i < n; i++){
        long long a;
        cin >> a;
        mp[a]++;
    }
    for (auto& m : mp){
        value.push_back(m.first * m.second);
    }
    sort(value.begin(), value.end());
    for (int i = 0; i < k; i++){
        if (!value.empty()){
            value.pop_back();
        }
    }
    // accumulateは第３引数の型となるため、0LLにする
    long long ans = accumulate(value.begin(), value.end(), 0LL);
    cout << ans << endl;

    return 0;
}
