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
using namespace std;
using ll = long long;

int main()
{
    string s;
    cin >> s;
    map<char, ll> num;
    ll len = s.size();
    for (int i = 0; i < len; i++){
        num[s[i]]++;
    }

    ll total = len * (len-1) / 2;
    bool has_same = false;
    for(const auto& n : num){
        if (n.second > 1){
            total -= (n.second * (n.second - 1) / 2);
            has_same = true;
        }
    }
    if (has_same){
        total++;
    }

    cout << total << endl;
    return 0;
}
