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
using ll = long long;

int judge(char a, char b){
    if (a == b) return -1;
    if (a == 'G' && b == 'P') return 1;
    if (a == 'C' && b == 'G') return 1;
    if (a == 'P' && b == 'C') return 1;
    return 0;
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<string> s(2 * n);
    for (int i = 0; i < 2 * n; i++){
        cin >> s[i];
    }
    vector<pair<int, int>> rank(2 * n);
    for (int i = 0; i < 2 * n; i++){
        rank[i] = {0, i};
    }

    for (int j = 0; j < m; j++){
        for (int i = 0; i < n; i++){
            int player1 = rank[2*i].second;
            int player2 = rank[2*i+1].second;
            int result = judge(s[player1][j], s[player2][j]);
            if (result != -1){
                rank[2*i + result].first -= 1;
            }
        }
        // 1ラウンドごとに順位を再計算
        sort(rank.begin(), rank.end());
    }

    for (int i = 0; i < 2 * n; i++){
        cout << rank[i].second + 1 << "\n";
    }

    return 0;
}
