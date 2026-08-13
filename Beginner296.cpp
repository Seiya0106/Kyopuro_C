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
    ll n, x;
    cin >> n >> x;
    set<int> s;
    for (int i = 0; i < n; i++){
        int t;
        cin >> t;
        s.insert(t);
    }

    for (auto a : s){
        if (s.find(a+x) != s.end()){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
