"""
ABC 大学には N 人の一年生が在籍しています。
クラスは 2 つあり、学籍番号 i 番の生徒のクラスは C[i] 組です。
今日は期末試験が返却され、学籍番号 i 番の生徒の点数は P[i] 点でした。

以下の形式の質問が Q 個与えられるので、答えてください。
・学籍番号 L[i] ～ R[i] の 1 組生徒における、期末試験点数の合計
・学籍番号 L[i] ～ R[i] の 2 組生徒における、期末試験点数の合計
・これら 2 つをそれぞれ求めよ。

【制約】
・1 ≦ N ≦ 10^5
・1 ≦ C[i] ≦ 2
・0 ≦ P[i] ≦ 100
・1 ≦ Q ≦ 10^5
・1 ≦ L[i] ≦ R[i] ≦ N
・入力はすべて整数

7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6

63 261
"""

if __name__ == "__main__":
    N = int(input())
    C = []
    P = []
    sum1 = []
    sum1.append(0)
    sum2 = []
    sum2.append(0)

    for i in range(N):
        c,p = [int(x) for x in input().split(" ")]
        C.append(c)
        P.append(p)
        # 累積和計算，変化がない場合はそのままの値を入れる
        if c == 1:
            sum1.append(sum1[-1] + p)
            sum2.append(sum2[-1])
        elif c == 2:
            sum1.append(sum1[-1])
            sum2.append(sum2[-1] + p)
        else:
            print("err")


    Q = int(input())
    L = []
    R = []
    for i in range(Q):
        l,r = [int(x) for x in input().split(" ")]
        L.append(l)
        R.append(r)
    
    for i in range(Q):
        ans1,ans2 = 0,0
        ans1 = sum1[R[i]] - sum1[L[i]-1]
        ans2 = sum2[R[i]] - sum2[L[i]-1]
        print(ans1,ans2)