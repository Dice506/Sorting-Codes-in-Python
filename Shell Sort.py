def shell_sort(arr):
    """
    Shell Sort:
    - Description: An optimization of insertion sort that allows the exchange of far-apart elements. 
                   The idea is to arrange the elements so that they are partially sorted (based on gaps), 
                   which helps insertion sort be more efficient.
    - Time Complexity: O(n log n) in the best cases, O(n²) in the worst cases depending on the gap sequence.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example usage
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Sorted array is:", arr)
