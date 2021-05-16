"""
N 個の都市があり、それぞれ 1, 2, 3, ..., N と番号付けられています。
また、N-1 本の道路があり、i 本目の道路は都市 A[i] と都市 B[i] を双方向に結んでいます。
どの都市の間も、いくつかの道路を通って移動可能なものとなっています。

さて、あなたは整数 u, v (1 ≦ u < v ≦ N) を自由に選び、都市 u と v を双方向に結ぶ道路を 1 本だけ新設することができます。
そこで、以下で定められる値をスコアとします。
・同じ道を 2 度通らずにある都市から同じ都市まで戻ってくる経路における、通った道の本数 (この値はただ一つに定まる)
スコアとして考えられる最大の値を出力してください。

【制約】
・1 ≦ N ≦ 100000
・1 ≦ A[i] < B[i] ≦ N
・どの都市の間も、いくつかの道路を通って移動可能
・入力はすべて整数
5
1 2
2 3
3 4
3 5

4
"""

# 木の直径は最短距離計算を2回やる
# 今回都市名が1始まりに注意

from collections import deque

def getdist(start: int) -> list:
    # 幅優先探索(BFS)で最短距離計算
    queue = deque([start]) # スタート位置をセット
    dist = [None] * (N+1) # 距離を入れるリスト初期化
    dist[start] = 0 # 自分との距離は0

    while queue:
        pos = queue.popleft()
        for i in g[pos]:
            if dist[i] is None:
                dist[i] = dist[pos] + 1    
                queue.append(i)
    return dist

if __name__ == '__main__':
    N = int(input())
    g = [[] for _ in range(N+1)] # 隣接リスト
    for _ in range (N-1):
        a,b = [int(x) for x in input().split(' ')]
        # それぞれの都市に隣接している都市をリスト化
        g[a].append(b)
        g[b].append(a)
    # 頂点1からの最短距離を求める
    dist1 = getdist(1)

    # maxn1: 頂点 1 からの最短距離の最大値
    maxn1 = -1
    # maxid1: 頂点 1 から最も離れている（最短距離が長い）頂点
    maxid1 = -1
    for i in range(N):
        # 1始まりだからi+1
        if maxn1 < dist1[i+1]:
            maxn1 = dist1[i+1]
            maxid1 = i+1

    # 頂点 maxid1からの最短距離を求める
    dist2 = getdist(maxid1)
    maxn2 = -1
    for i in range(N):
        maxn2 = max(maxn2, dist2[i+1])

    # 道を追加したら答えなので＋1
    print(maxn2+1)