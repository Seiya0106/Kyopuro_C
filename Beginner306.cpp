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
    vector<int> ans;
    vector<int> cnt(n+1);
    for (int i = 0; i < 3*n; i++){
        int a;
        cin >> a;
        cnt[a]++;
        if (cnt[a] == 2){
            ans.push_back(a);
        }
    }

    for (int i = 0; i < n; i++){
        cout << ans[i] << " ";
    }
    cout << endl;
    return 0;
}
