import sys
sys.stdin = open("input.txt", "r")


def DFS(L, s):
    global cnt  # 이거 해줘야 에러 안 남
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1  # global 해줘야 됨
    else:
        for i in range(s, n+1):  # s부터 n까지
            res[L] = i
            DFS(L+1, i+1)  # 레벨은 1 증가, 가지 숫자 + 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*(n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)