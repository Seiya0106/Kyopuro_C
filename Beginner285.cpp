#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int main(){
    string s;
    cin >> s;
    long long power = 1;
    long long ans = 0;
    for (int i = s.size() - 1; i >= 0; i--){
        ans += power * (int(s[i]) - 64);
        power *= 26;
    }
    cout << ans << endl;
}
