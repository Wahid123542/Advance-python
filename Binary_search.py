_list = [1, 3, 5, 6, 7, 8, 9]
target = 5

def binary_search(arr, target):
    if len(arr) == 0:
        return "not found"

    mid = len(arr) // 2

    if arr[mid] == target:
        return "found"
    elif target < arr[mid]:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)
