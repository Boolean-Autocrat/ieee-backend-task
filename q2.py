# program to print a spiral pattern of numbers


def spiral_pattern(n):
    # first, i initialize a 2D array of size n x n (filled with 0s)
    spiral_arr = [[0] * n for _ in range(n)]
    # setting initial direction to right
    direct = "rt"
    top, bottom, left, right = 0, n - 1, 0, n - 1
    value = 1
    while value <= n * n:
        if direct == "rt":
            for i in range(left, right + 1):
                spiral_arr[top][i] = value
                value += 1
            top += 1
            direct = "d"
        elif direct == "d":
            for i in range(top, bottom + 1):
                spiral_arr[i][right] = value
                value += 1
            right -= 1
            direct = "lt"
        elif direct == "lt":
            for i in range(right, left - 1, -1):
                spiral_arr[bottom][i] = value
                value += 1
            bottom -= 1
            direct = "up"
        elif direct == "up":
            for i in range(bottom, top - 1, -1):
                spiral_arr[i][left] = value
                value += 1
            left += 1
            direct = "rt"

    # printing the pattern
    for row in spiral_arr:
        print(*row)


# Test cases
spiral_pattern(3)
print()
spiral_pattern(4)
print()
# User input
n = int(input("Enter a number: "))
spiral_pattern(n)
