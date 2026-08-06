#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<ll>> b(n, vector<ll>(m));
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            cin >> b[y][x];
        }
    }

    bool ok = true;

    // 基準が合っているか
    if ((b[0][0] - 1) % 7 + m > 7) {
        ok = false;
    }

    // 2. 隣り合う要素の関係性をチェック
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            if (x + 1 < m && b[y][x] + 1 != b[y][x + 1]) {
                ok = false;
            }
            if (y + 1 < n && b[y][x] + 7 != b[y + 1][x]) {
                ok = false;
            }
        }
    }

    if (ok) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
