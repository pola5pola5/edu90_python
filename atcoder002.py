"""
長さ N の正しいカッコ列をすべて、辞書順に出力してください。
ただし、正しいカッコ列は次のように定義されています :
() は正しいカッコ列である
S が正しいカッコ列であるとき、文字列 ( +S+ ) は正しいカッコ列である
 S,T が正しいカッコ列であるとき、文字列 S+Tは正しいカッコ列である
それ以外の文字列はすべて、正しいカッコ列でない

4
()()
(())
"""

# 小さい制約は全探索
# 二進数に置き換える(bit全探索)
# ・(と)の数が同じ
# ・全てのiについて左からi文字目までの時点で(の数が)の数以上
# 上記2点を満たすのが必要十分

def hantei(S: str) -> bool:
    dep = 0
    for i in range(len(S)):
        # (と)の出現をプラマイで表現
        if S[i] == "(":
            dep += 1
        if S[i] == ")":
            dep -= 1
        # )の方が先に多く出るのはおかしい
        if dep < 0:
            return False
    if dep == 0:
        return True
    return False

if __name__ == '__main__':
    N = int(input())
    # 全通り試すための2^nループ
    for i in range(2**N):
        Candidate = ""
        for j in range(N):
            j = N - 1 - j
            # &はビットAND
            if (i & 1<<j) == 0:
                Candidate += "("
            else:
                Candidate += ")"
        # print(Candidate)  
        I = hantei(Candidate)
        if I:
            print(Candidate)              
