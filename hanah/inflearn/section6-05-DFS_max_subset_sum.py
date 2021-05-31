'''
# 바둑이 승차(DFS)

철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태울수가 없다. 
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.

N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 
둘째 줄부터 N마리 바둑이의 무게가 주어진다.

▣ 출력설명
첫 번째 줄에 가장 무거운 무게를 출력한다.
▣ 입력예제 1 
259 5
81
58
42 
33 
61

▣ 출력예제 1 
242

'''

c, n = map(int, input().split())
a = [int(input()) for _ in range(n)]
check = [0] * n
total = sum(a)
max = 0

def dfs(L, sum, cur_sum): # L는 a의 인덱스이자 상태트리의 레벨, sum은 index L전 까지의 합, cur_sum은 L레벨 까지 따져봤을 때의 총 합(부분집합에 포함이 되건 안되건)
    global max
    
    if sum > c:
        return

    if sum + (total - cur_sum) < max: # L레벨 이후에 있는 것들을 다 넣는다 쳐도 max보다 작음 >> 더 확인할거 없이 종료
        return

    if L == n:
        if sum > max:
            max = sum
    else:
        dfs(L + 1, sum + a[L], cur_sum + a[L]) # L째 요소를 부분집합에 포함시킴
        dfs(L + 1, sum, cur_sum + a[L]) # L번째 요소를 부분집합에 포함시키지 않음

    
dfs(0, 0, 0)
print(max)
