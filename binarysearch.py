B = [-3, -1, 0, 1, 4, 7]

#Native O(n) searching:
if 7 in B:
    print(True)

#Traditional Binary Search - Looking if a numer is in array
#Time :O(log n )
#Space: O(1)
def binary_search(arr, target):
    N = len(B)
    L = 0
    R = N-1

    while L <= R:
        M = L + ((R-L) // 2)

    if arr[M] == target:
        return True
    elif target < arr[M]:
        R = M-1
    else:
        L = M+1
    return False

binary_search(B, -1)

#Based on a condition
#[F, F, F, T, T, T]

C = [False, False, False, False, True, True, True, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N -1

    while L < R:
        M = (L+R) // 2

        if C[M]:
            R = M
        else:
            L = M + 1

    return L

binary_search_condition(B)