#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#include <numbers>
#include <iomanip>
#include <queue>
using namespace std;

int main()
{
    int q;
    cin >> q;
    // 小さい順に並ぶ優先度つきキュー
    priority_queue<int, vector<int>, greater<int>> que;
    for (int i = 0; i <q; i++){
        int t, h;
        cin >> t >> h;
        if (t == 1){
            que.push(h);
        }
        else if(t == 2){
		        // 先頭(最小値)がh以下の間、削除し続ける
            while (!que.empty() && que.top()  <= h){
                que.pop();
            }
        }
        cout << que.size() << endl;
    }
}
