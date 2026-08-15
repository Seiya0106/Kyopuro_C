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
using namespace std;
using ll = long long;

int main()
{
    string s;
    cin >> s;
    int i = 0;
    int ans = 0;
    while (true){
        if (i >= s.size()) break;

        if (s[i] == '0' && i+1 < s.size() && s[i+1] == '0'){
            i = i + 2;
        }
        else{
            i++;
        }
        ans++;
    }

    cout << ans << endl;
    return 0;
}
