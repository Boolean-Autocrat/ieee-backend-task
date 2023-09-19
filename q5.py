# max alternating sum of array of length n


def max_alternating_sum(arr, n):
    for i in range(n):
        arr[i] = abs(arr[i])

    subtract_arr = sorted(arr[1:n:2], reverse=True)
    addition_arr = sorted(arr[0:n:2])

    if addition_arr[0] < subtract_arr[0]:
        addition_arr[0], subtract_arr[0] = subtract_arr[0], addition_arr[0]
    return sum(addition_arr) - sum(subtract_arr)


test_cases = int(input())
results = []

for case in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_alternating_sum(arr, n)
    results.append(result)

for result in results:
    print(result)
