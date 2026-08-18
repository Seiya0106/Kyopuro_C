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
    string s, t;
    cin >> s >> t;
    int len = s.size();
    int ans = 0;
    for (int i = 0; i < len; i++){
        if (s[i] != t[i]){
            ans = i+1;
            break;
        }
    }
    if (ans == 0){
        ans = t.size();
    }

    cout << ans << endl;
    return 0;
}
