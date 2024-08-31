def tim_sort(arr):
    """
    Tim Sort:
    - Description: Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. 
                   It performs well on many kinds of real-world data by breaking the data into small chunks, 
                   sorting them using insertion sort, and then merging the sorted chunks using merge sort.
    - Time Complexity: O(n log n)
    """
    arr.sort()  # Python's built-in sort() uses TimSort

# Example usage
arr = [12, 4, 6, 23, 9, 34, 1]
tim_sort(arr)
print("Sorted array is:", arr)
