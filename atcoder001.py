"""
左右の長さが 
L[cm] のようかんがあります。 
N個の切れ目が付けられており、左から 
i番目の切れ目は左から 
Ai[cm] の位置にあります。
あなたは N個の切れ目のうち K個を選び、ようかんを 
K+1個のピースに分割したいです。そこで、以下の値を スコア とします。

K+1個のピースのうち、最も短いものの長さ（cm 単位）
スコアが最大となるように分割する場合に得られるスコアを求めてください。
  
# 入力形式
N L
K
A[1] A[2] A[3] ... A[N]


"""
# 答えで二分探索

# coding: utf-8
import itertools

def solve(M: int) -> bool:
    cnt,pre = 0,0

    for i in range(N):
        # print(f"a[{i}]",A[i])
        # print("cnt,pre,M",cnt,pre,M)
        if int(A[i]) - pre >= M and L - int(A[i]) >= M:
            cnt += 1
            pre = int(A[i])
    if cnt >= K:return True
    return False

if __name__ == '__main__':
    data = input().rstrip().split(" ")
    N = int(data[0])
    L = int(data[1])
    K = int(input())
    A = input().rstrip().split(" ")

    # 答えで二分探索（めぐる式二分探索法)
    left = -1
    right = L + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        # print("r,l,m",right,left,mid)
        if solve(mid) == False:
            right = mid
        else:
            left = mid
    print(left)