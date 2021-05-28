"""
H 行 W 列のマス目があります。上から i (1 ≦ i ≦ H) 行目、左から j (1 ≦ j ≦ W) 列目にあるマス (i, j) には、整数 A[i][j] が書かれています。

すべてのマス (i, j) [1 ≦ i ≦ H, 1 ≦ j ≦ W] について、以下の値を求めてください。
・マス (i, j) と同じ行または同じ列にあるマス（自分自身を含む）に書かれている整数をすべて合計した値

【制約】
・1 ≦ H ≦ 2000
・1 ≦ W ≦ 2000
・1 ≦ A[i][j] ≦ 99
・入力はすべて整数

4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3

28 28 25 26
39 33 40 34
38 38 36 31
41 41 39 43

"""
# import numpy as np #pypyだと使えない

if __name__ == '__main__':
    H,W = [int(x) for x in input().split(" ")]
    A = []
    B = [[0] * W for i in range(H)]
    for _ in range (H):
        a = [int(x) for x in input().split(" ")]
        A.append(a)
    # Column = np.sum(A,axis=0)
    # Row = np.sum(A,axis=1)
    Column = []
    Row = []
    for i in range (H):
        r = 0
        for j in range (W):
            r += A[j][i]
        Column.append(r)
        Row.append(sum(A[i]))

    for i in range(H):
        for j in range(W):
            B[i][j] = Row[i] + Column[j] - A[i][j]
            print(B[i][j], end = " ")
        print()