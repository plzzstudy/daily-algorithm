import sys
sys.stdin = open("input.txt", "r")


def DFS(v):
    if v > 7:
        return
    else:
        # 전위순회
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)


if __name__ == "__main__":
    DFS(1)
