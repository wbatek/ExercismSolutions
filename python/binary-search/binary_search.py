def find(search_list, value):
    left, right = 0, len(search_list) - 1
    while left <= right:
        mid = (left + right) // 2
        val = search_list[mid]
        if val == value:
            return mid
        if val < value:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("value not in array")
