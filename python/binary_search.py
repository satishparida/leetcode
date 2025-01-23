def binary_search_linear(arr: list, x):
    """
    Time Complexity: O(logN)
    Space Complexity O(1) -> Function calls do not exist simultaneously on the call stack
    """
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = low + (high - low) // 2 # this is how mid is caluculated to avoid int overflow for very long integers if we do (low + high)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid +1 # discarding the left half, as the number exists in right half
        elif arr[mid] > x:
            high = mid-1 # discarding the right half, as the number exists in left half
    return -1

# t = binary_search_linear([0,1,2,3,4,5,6,7,8,9], 10)
# print(t)

def binary_search_recursive(arr: list, low: int, high: int, x):
    """
    Time Complexity: O(logN)
    Space Complexity O(logN) -> Function calls exist simultaneously on the call stack
    """
    if high >= low:
        mid = low + (high - low)//2
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        elif arr[mid] < x:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

# a = [0,1,2,3,4,5,6,7,8,9]
# t = binary_search_recursive(a, 0, len(a)-1, 10)
# print(t)
