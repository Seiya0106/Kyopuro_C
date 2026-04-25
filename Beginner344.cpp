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
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++){
        cin >> b[i];
    }
    int l;
    cin >> l;
    vector<int> c(l);
    for (int i = 0; i < l; i++){
        cin >> c[i];
    }
    int q;
    cin >> q;
    vector<int> x(q);
    for (int i = 0; i < q; i++){
        cin >> x[i];
    }
    vector<bool> nums(3 * pow(10, 8) + 1);
    for (auto d : a){
        for (auto e : b){
            for (auto f : c){
                nums[d+e+f] = true;
            }
        }
    }
    for (auto w : x){
        if (nums[w]){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }

    return 0;
}
