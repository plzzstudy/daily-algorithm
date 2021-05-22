# 이분검색

# 임의의 N개의 숫자가 입력으로 주어집니다. 
# N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 
# 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 
# 단 중복값은 존재하지 않습니다.

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = 0
e = n
while s <= e:
    mid = (s+e)//2
    if m > a[mid]:
        s = mid
    elif m < a[mid]:
        e = mid
    else:
        break
print(mid+1)


# solution
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1