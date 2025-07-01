def binary_search(arr, low, high, x):
    # Base case: If the search range is valid
    if high >= low:
        # Find the middle index
        mid = (high + low) // 2

        # If element is at the middle
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, search in the left half
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element is in the right half
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not in the array
        return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14]
    x = 10  # Element to search for

    result = binary_search(arr, 0, len(arr) - 1, x)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")
