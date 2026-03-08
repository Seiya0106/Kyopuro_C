// 後半のロジックは自分で考えたが、作成方法がわからなかったためAI作成
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#include <numeric>
#include <algorithm>
using namespace std;

int main(){
    int n, q;
    cin >> n >> q;
    vector<pair<int, int>> a(n);
    int s;
    for (int i = 0; i < n; i++){
        cin >> a[i].first;
        a[i].second = i+1;
    }
    sort(begin(a), end(a));
    int k;
    for (int i = 0; i < q; i++){ // ← n ではなく q 回
        cin >> k;
        vector<int> b(k);
        for (int j = 0; j < k; j++){
            cin >> b[j];
        }

        // b に含まれているかを高速に判定するため set に入れる
        set<int> removed(begin(b), end(b));

        // a は「値で昇順ソート済み」なので、小さ��値から順に
        // 「取り出されていないボール」を見つけたらそれが答え（最小値）
        for (int x = 0; x < n; x++){
            // a[x].second (= 元のボール番号) が removed に含まれていなかったら出力
            if (removed.find(a[x].second) == removed.end()){
                cout << a[x].first << "\n";
                break;
            }
        }
    }
}
