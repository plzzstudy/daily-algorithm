# 침몰하는 타이타닉

# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 
# 유람선에는 N명의 승객이 타고 있습니다. 구명보트를 타고 탈출해야 하는데 
# 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있 으며, 
# 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

from collections import deque

n, m=map(int, input().split())
w=list(map(int, input().split()))

w.sort()
w=deque(w)
cnt=0
while w:
    if len(w)==1:
        cnt+=1
        break
    if w[0]+w[-1]>m:
        w.pop()
        cnt+=1
    else:
        w.popleft()
        w.pop()
        cnt+=1
print(cnt)