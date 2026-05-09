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
    string s;
    cin >> s;
    long long result = 0;
    int start_i = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == s[i+1] || i + 1 == s.size()){
            result += (long long)(i - start_i + 1) * (i - start_i + 2) / 2;
            start_i = i + 1;
        }
    }
    cout << result % 998244353 << endl;
}
