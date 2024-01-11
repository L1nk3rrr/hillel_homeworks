def find_lake_depth(heights):
    if not heights or len(heights) <= 2:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height to the left of each position
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Calculate the maximum height to the right of each position
    right_max[n - 1] = heights[n - 1]
    # n - 2, -1, -1 -> going from the end (right)
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate the depth of the lake at each position
    depths = [min(left_max[i], right_max[i]) - heights[i] for i in range(n)]

    # Return the maximum depth
    return max(0, max(depths))

assert find_lake_depth([]) == 0
assert find_lake_depth([0]) == 0
assert find_lake_depth([0, 1]) == 0
assert find_lake_depth([2, 1, 4]) == 1
assert find_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6
assert find_lake_depth([5, 4, 3, 2, 1]) == 0
assert find_lake_depth([1, 2, 3, 4, 5]) == 0
assert find_lake_depth([1, 2, 1, 3, 4, 5]) == 1
assert find_lake_depth([1, 2, 3, 2, 1]) == 0
assert find_lake_depth([3, 4, 5, 1, 3, 2, 6]) == 4
assert find_lake_depth([3, 3, 3, 3, 3]) == 0