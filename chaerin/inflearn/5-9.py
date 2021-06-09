# 아나그램

# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 
# A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 
# 즉 어느 한 단어를 재 배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세요. 아나그램 판별시 대소문자가 구분됩니다.

first=input()
second=input()
d=dict()

for i in first:
    d[i]=d.get(i, 0)+1
for i in second:
    d[i]=d.get(i, -1)-1
for key, val in d.items():
    if val!=0:
        print('NO')
        break
else:
    print('YES')


# solution1(딕셔너리1)
a=input()
b=input()
str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')


# solution2(딕셔너리2)
a=input()
b=input()
sH=dict()

for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if sH.get(x)>0:
        print('NO')
        break
else:
    print('YES')


# solution(리스트)
a=input()
b=input()
str1=[0]*52  # 대문자 26개+소문자26개
str2=[0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1    # ord: 문자를 아스키 코드값으로 변환. 대문자: 65~90, 소문자: 97~122
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1    

for i in range(52):
    if str1[i]!=str2[i]:
        print('NO')
        break
else:
    print('YES')