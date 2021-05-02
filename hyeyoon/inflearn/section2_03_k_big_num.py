import sys

n, k = map(int, input().split())
cards = list(map(int, input().split()))
three_list = []
sum_list = []
for i in cards:
    for j in cards:
        for 
    if i <= 2:
        three_list.append(cards[i])
        sum_list.append(sum(three_list))
    else:
        break

sorted_cards = sum_list.sort(reverse=True)
a = set(sorted_cards)
print(a[k-1])