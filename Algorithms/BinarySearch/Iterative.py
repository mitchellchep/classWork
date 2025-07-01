def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    array = [10, 20, 30, 40, 50, 60, 70]
    target = 50

    result = binarySearch(array, target, 0, len(array) - 1)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
