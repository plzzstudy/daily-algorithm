# 이진트리 순회(깊이우선탐색)

def DFS(v):
    if v>7:
        return
    else:
        #print(v, end=' ')   # 전위순회 출력
        DFS(v*2)
        #print(v, end=' ')   # 중위순회 출력
        DFS(v*2+1)
        #print(v, end=' ')   # 후위순회 출력

if __name__=="__main__":
    DFS(1)