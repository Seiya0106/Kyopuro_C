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
using namespace std;

int main()
{
    long long n;
    cin >> n;
    n--;
    vector<int> a;
    vector<int> even = { 0, 2, 4, 6, 8 };
    while (true){
        a.push_back(n%5);
        n /= 5;
        if (n <= 0){
            break;
        }
    }
    for (int i = a.size()-1; i >= 0; i--){
        cout << even[a[i]];
    }
    cout << endl;
}
