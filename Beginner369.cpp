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
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    ll total = (ll)n + n-1;
    int length = 2;
    for (int i = 2; i < n; i++){
        if (a[i]-a[i-1] == a[i-1]-a[i-2]){
            length++;
            total += length-2;
        }
        else{
            length = 2;
        }
    }

    cout << total << endl;
    return 0;
}
