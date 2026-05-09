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
    multiset<long long> tree;
    for (int i = 0; i < q; i++){
        long long n, h;
        cin >> n >> h;
        if (n == 1){
            tree.insert(h);
        }
        else{
            auto it_start = tree.lower_bound(1);
            auto it_end = tree.upper_bound(h);
            tree.erase(it_start, it_end);
        }
        cout << tree.size() << endl;
    }
}
