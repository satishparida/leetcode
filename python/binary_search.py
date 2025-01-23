def binary_serch(arr: list, x):
    low = 0
    high = len(arr)-1
    # for i in range(0, len(arr)):
    #     print(arr[i])
    while high>low:
        mid = low + high // 2
        print(mid, arr[mid])

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid
        elif arr[mid] > x:
            high = mid



binary_serch([0,1,3,5,6,7,8,9,10,11], 10)