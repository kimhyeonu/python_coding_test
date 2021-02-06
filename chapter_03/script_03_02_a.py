# 문제
# '큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 현우는 본인만의 방식으로 다르게 사용하고 있다.
# 현우의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 현우의 큰 수의 법칙에 따른 결과를 출력하시오.

# 입력 조건
# 첫째 줄에 N(2 <= N < 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건
# 첫째 줄에 현우의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력 예시
# 46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_number = data[n - 1]
second_number = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_number
        m -= 1
    
    if m == 0:
        break

    result += second_number
    m -= 1

print(result)
