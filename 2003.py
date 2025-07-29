N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    current_sum = 0
    for j in range(i, N):
        current_sum += A[j]
        if current_sum == M:
            count += 1
        if current_sum > M:
            break

print(count)
