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
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<long long, long long> dict;
    for (int i = 0; i < n; i++){
        long long a, c;
        cin >> a >> c;
        if (dict.count(c) == 0){   // keyがない場合
            dict[c] = a;
        }
        else{
            dict[c] = min(dict[c], a);
        }
    }
    long long max_min = 0;
    for (auto d : dict){
        max_min = max(max_min, d.second);
    }
    cout << max_min << endl;
}
