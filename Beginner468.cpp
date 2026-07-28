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

int main() 
{
    int n;
    cin >> n;
    vector<int> p(n);
    vector<int> q(n);
    for (int i = 0; i < n; i++){
        cin >> p[i];
    }
    for (int i = 0; i < n; i++){
        cin >> q[i];
    }

    vector<int> v(n);
    for (int i = 0; i < n; i++){
        v[i] = i+1;
    }
    int current_index = 0;
    int p_index = 0, q_index = 0;
    do{
        if (p == v){
            p_index = current_index;
        }
        if (q == v){
            q_index = current_index;
        }
        current_index++;
    }while (next_permutation(v.begin(), v.end()));

    if (p_index >= q_index){
        cout << 0 << endl;
    }
    else{
        cout << q_index - p_index - 1 << endl;
    }
    return 0;
}
