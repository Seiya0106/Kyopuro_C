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
    string s;
    int k;
    cin >> s >> k;
    sort(s.begin(), s.end());
    int cnt = 1;
    do{
        if (cnt == k){
            cout << s << endl;
        }
        cnt++;
    }while(next_permutation(s.begin(), s.end()));
    return 0;
}
