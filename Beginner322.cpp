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
    int n, m;
    cin >> n >> m;
    vector<int> a(m);
    for (int i = 0; i < m; i++){
        cin >> a[i];
    }
    int idx = 0;
    for (int i = 1; i < n+1; i++){
        if (a[idx] >= i){
            cout << a[idx] - i << endl;
        }
        else{
            idx++;
            cout << a[idx] - i << endl;
        }
    }

    return 0;
}
