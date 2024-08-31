def bucket_sort(arr):
    """
    Bucket Sort:
    - Description: Bucket Sort distributes elements into several buckets, each containing a range of values.
                   Each bucket is then sorted individually, often using insertion sort or another simple sorting method.
                   Finally, the sorted buckets are combined to form the sorted array.
    - Time Complexity: O(n + k), where n is the number of elements and k is the number of buckets.
    """
    if len(arr) == 0:
        return

    # Step 1: Create buckets and distribute elements
    bucket_count = 10  # Number of buckets
    max_value = max(arr)
    bucket_list = [[] for _ in range(bucket_count)]

    # Distribute array elements into buckets based on their value
    for num in arr:
        index = int(num / max_value * (bucket_count - 1))
        bucket_list[index].append(num)

    # Step 2: Sort each bucket using a simple sort (insertion sort in this case)
    for i in range(bucket_count):
        bucket_list[i] = sorted(bucket_list[i])

    # Step 3: Concatenate sorted buckets
    sorted_arr = []
    for bucket in bucket_list:
        sorted_arr.extend(bucket)

    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

# Example usage
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("Sorted array is:", arr)
