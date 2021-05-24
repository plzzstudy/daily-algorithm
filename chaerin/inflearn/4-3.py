# 뮤직비디오(결정알고릐즘)

# ▣ 입력설명
# 첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 
# 다음 줄에는 조영필이 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다.
# 부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.

# ▣ 출력설명
# 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.

# 필요한 DVD 갯수를 구하기 위한 함수
def Count(capacity):
    cnt=1   # DVD 갯수
    sum=0   # DVD 한장에 누적된 곡들의 길이
    for x in songs:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
songs=list(map(int, input().split()))
maxx=max(songs) # DVD 한장은 무조건 제일 용량이 큰 노래를 담을 수 있어야 한다.
lt=1
rt=sum(songs)
result=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        result=mid
        rt=mid-1
    else:
        lt=mid+1
print(result)
