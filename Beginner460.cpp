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
using namespace std;


int main()
{
    int n, m;
    cin >> n >> m;
    vector<long long> a(n);
    vector<long long> b(m);
    for (int i = 0; i < a.size(); i++){
        cin >> a[i];
    }
    for (int i = 0; i < b.size(); i++){
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int x, y;
    x = 0, y = 0;
    int total = 0;
    while (x < n && y < m){
        if (b[y] <= a[x] * 2){
            total++;
            x++;
            y++;
        }
        else{
            x++;
        }
    }
    cout << total << endl;
}
