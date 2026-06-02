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
    int n, m;
    cin >> n >> m;
    // 隣接リストの初期化
    vector<vector<int>> g(n);
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        // 1-indexed から 0-indexed への変換
        g[x - 1].push_back(y - 1);
    }

    queue<int> q;
    vector<bool> d(n, false); // 訪問済みフラグ（Pythonの d = [False] * n）

    // 始点（ノード0）の設定
    q.push(0);
    d[0] = true;

    // 幅優先探索 (BFS)
    while (!q.empty()) {
        int x = q.front();
        q.pop();

        for (int i : g[x]) {
            if (d[i]) {
                continue;
            }
            d[i] = true;
            q.push(i);
        }
    }

    // d の中で true になっている要素の数をカウント
    int ans = count(d.begin(), d.end(), true);
    cout << ans << "\n";

    return 0;
}
