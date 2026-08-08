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
    vector<ll> x(n);
    vector<ll> y(n);
    for (int i = 0; i < n; i++){
        cin >> x[i] >> y[i];
    }

    int total = 0;
    for (int i = 0; i < n; i++){
        for (int j = i+1; j < n; j++){
            for (int k = j+1; k < n; k++){
                if ((x[j]-x[i]) * (y[k]-y[i]) - (x[k]-x[i]) * (y[j]-y[i]) != 0){  // 面積が0でないことで三角形であるかを判断
                    total++;
                }
            }
        }
    }

    cout << total << endl;
    return 0;
}
