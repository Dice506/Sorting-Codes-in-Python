MIN_RUN = 32

def insertion_sort(arr, left, right):
    """
    Performs insertion sort on the sublist of arr from index `left` to `right`.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays of arr.
    First subarray is arr[left:mid+1].
    Second subarray is arr[mid+1:right+1].
    """
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = [], []
    
    for i in range(len1):
        left_part.append(arr[left + i])
    for i in range(len2):
        right_part.append(arr[mid + 1 + i])

    i, j, k = 0, 0, left
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    """
    Tim Sort:
    - Description: Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. 
                   It divides the array into small subarrays of a minimum run size, sorts them using 
                   insertion sort, and then merges them using merge sort.
    - Time Complexity: O(n log n)
    """
    n = len(arr)
    # Step 1: Sort small chunks of the array with insertion sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge the sorted chunks
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

# Example usage
arr = [12, 4, 6, 23, 9, 34, 1, 8, 0, 5, 33, 20, 21, 22, 3, 19, 31, 2, 18]
tim_sort(arr)
print("Sorted array is:", arr)
