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
    vector<vector<int>> a(9, vector<int>(9));
    for (int y = 0; y < 9; y++){
        for (int x = 0; x < 9; x++){
            cin >> a[y][x];
        }
    }

    // 横の判定
    for (int y = 0; y < 9; y++) {
        set<int> st;
        for (int x = 0; x < 9; x++) {
            st.insert(a[y][x]);
        }
        if (st.size() != 9) {
            cout << "No" << endl;
            return 0;
        }
    }

    // 縦の判定
    for (int x = 0; x < 9; x++) {
        set<int> st;
        for (int y = 0; y < 9; y++) {
            st.insert(a[y][x]);
        }
        if (st.size() != 9) {
            cout << "No" << endl;
            return 0;
        }
    }

    // 3 * 3 の判定
    for (int by = 0; by < 9; by += 3) {
        for (int bx = 0; bx < 9; bx += 3) {
            set<int> st;
            for (int dy = 0; dy < 3; dy++) {
                for (int dx = 0; dx < 3; dx++) {
                    st.insert(a[by + dy][bx + dx]);
                }
            }
            if (st.size() != 9) {
                cout << "No" << endl;
                return 0;
            }
        }
    }

    cout << "Yes" << endl;
    return 0;
}
