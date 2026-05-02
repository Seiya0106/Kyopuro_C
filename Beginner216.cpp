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

int main()
{
    long long n;
    cin >> n;
    string s = "";
    while (n > 0){
        if (n % 2 == 1){
            s += 'A';
            n--;
        }
        else{
            s += 'B';
            n /= 2;
        }
    }
    reverse(s.begin(), s.end());
    cout << s << endl;
}
