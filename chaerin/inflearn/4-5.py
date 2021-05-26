# 회의실 배정(그리디)

# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다. 
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 
# 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 
# 단, 회의는 한번 시작하면 중간에 중 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

# 문제 풀이
# 1. 끝나는 시간을 기준으로 회의 정렬
# 2. 끝나는 시간과 다음 회의의 시작시간을 비교
# 3. 시작시간이 크거나 같으면 회의 진행 가능

n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s,e))   # tuple 형태로 리스트에 추가
meeting.sort(key=lambda x : (x[1], x[0]))   # x[1]이 정렬의 우선순위
end=0
cnt=0
for s, e in meeting:
    if s>=end:
        end=e
        cnt+=1
print(cnt)