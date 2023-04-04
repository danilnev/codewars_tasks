def binary_array_to_number(arr):
    result = 0
    for i, num in enumerate(reversed(arr), 0):
        if num == 1:
            result += 2 ** i
    return result
