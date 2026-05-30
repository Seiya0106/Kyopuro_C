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
    int length = s.size();
    vector<int> index;
    for (int i = 0; i < length; i++){
        if (s[i] == 'C'){
            index.push_back(i);
        }
    }
    long long total = 0;
    for (auto& idx : index){
        total += min(idx+1, length - idx);
    }
    cout << total << endl;
}
