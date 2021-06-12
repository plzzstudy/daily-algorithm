# 재귀함수를 이용한 이진수 출력

# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
# 단 재귀함수를 이용해서 출력해야 합니다.

# solution1
def DFS(x):
    if x==0:
        return
    else:
        print(x%2, end='')
        DFS(x//2)

if __name__=="__main__":
    n=int(input())
    DFS(n)

#solution2
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')
    
if __name__=="__main__":
    n=int(input())
    DFS(n)