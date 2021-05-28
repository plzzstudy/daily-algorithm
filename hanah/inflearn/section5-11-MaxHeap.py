'''
# 최대 힙

최대힙은 완전이진트리로 구현된 자료구조입니다.
그 구성은 부모 노드값이 왼쪽자식과 오른쪽 자식노드의 값보다 크게 트리를 구성하는 것입니다.
그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 큰 값이 저장되어 있습니다. 
예를 들어 5 3 2 1 4 6 7순으로 입력되면 최대힙 트리는 아래와 같이 구성됩니다.

(그림 생략)

최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요. 
1) 자연수가 입력되면 최대힙에 입력한다.
2) 숫자 0 이 입력되면 최대힙에서 최댓값을 꺼내어 출력한다.
  (출력할 자료가 없으면 -1를 출력한다.) 
3) -1이 입력되면 프로그램 종료한다.

▣ 입력설명
첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정 수형 범위에 있다.

▣ 출력설명
2) 연산을 한 결과를 보여준다.

▣ 입력예제 1
5
3 
6 
0 
5 
0 
2
4
0 
-1

▣ 출력예제 1 
6
5
5
'''

import sys

# 파이썬에서는 최대 힙을 제공하지 않는다. 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.
import heapq as hq

a = []
while True:
    n = int(sys.stdin.readline().rstrip())
    
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
