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
using ll = long long;

int main() 
{
    string s;
    cin >> s;
    int len = s.size();
    int front = 0, last = len-1;
    while(true){
        if (abs(front - last) <= 1){    // 最後の判定
            cout << "Yes" << endl;
            return 0;
        }

        if (s[front] == s[last]){
            front++;
            last--;
        }
        else if (s[front] != 'a' && s[last] == 'a'){
            last--;
        }
        else{
            cout << "No" << endl;
            return 0;
        }
    }
}
