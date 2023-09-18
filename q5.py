# alternating sum of array of length n
def max_alternating_sum(arr, n):
    for _ in range(n):
        arr[_] = abs(arr[_])

    # sorting the addition array in ascending order (sorted just returns it)
    addition_arr = sorted(arr[0:n:2])

    # sorting the subtraction array in descending order (because we need the largest number)
    subtract_arr = sorted(arr[1:n:2], reverse=True)

    # if the first element of the addition array
    # is smaller than the first element of the subtraction array
    # then we swap them
    if addition_arr[0] < subtract_arr[0]:
        addition_arr[0], subtract_arr[0] = subtract_arr[0], addition_arr[0]

    # since we need the largest alternating sum and we
    # have swapped the largest number to the addition array
    # we can just add the addition array and subtract the subtraction array

    return sum(addition_arr) - sum(subtract_arr)


cases = int(input())
results = []

for case in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_alternating_sum(arr, n)
    results.append(result)

for result in results:
    print(result)
