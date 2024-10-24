def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is at mid
        if arr[mid] == target:
            return mid

        # Determine which part of the array is sorted
        if arr[left] <= arr[mid]:
            # Left part is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search in the left part
            else:
                left = mid + 1   # Search in the right part
        else:
            # Right part is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search in the right part
            else:
                right = mid - 1  # Search in the left part

    # Target not found
    return -1

# Driver code
if __name__ == "__main__":
    # Example rotated sorted array
    arr = [15, 18, 2, 3, 6, 12]
    
    # Element to search for
    target = 3
    
    # Search in the rotated sorted array
    result = search_rotated_array(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
