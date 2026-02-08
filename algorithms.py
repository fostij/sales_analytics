"""
algorithms.py

Contains custom implementations of sorting and searching
algorithms for educational and performance comparison purposes.
"""


# O(n2)
def bubble_sort(arr):
    """
    Custom bubble sort implementation.

    Time Complexity: O(n^2)
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(n)
def linear_search(arr, target):
    """
    Custom linear search implementation.

    Time Complexity: O(n)
    """
    for x in arr:
        if x == target:
            return True
    return False