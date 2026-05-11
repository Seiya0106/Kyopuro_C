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
    int q;
    cin >> q;
    multiset<long long> s;
    for (int i = 0; i < q; i++){
        int n;
        cin >> n;
        if (n == 1){
            long long x;
            cin >> x;
            s.insert(x);
        }
        else if (n == 2){
            long long x, c;
            cin >> x >> c;
            for (int j = 0; j < c; j++){
                auto it = s.find(x);
                if (it != s.end()){
                    s.erase(s.find(x));
                }
                else{
                    break;
                }
            }
        }
        else{
            auto maxIt = prev(s.end());
            auto minIt = s.begin();
            cout << *maxIt - *minIt << endl;
        }
    }
}
