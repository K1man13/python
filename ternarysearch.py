# Ternary Search implementation
def ternary_search(arr, left, right, target):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Check if the target is at mid1 or mid2
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # If target is in the left one-third
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        # If target is in the right one-third
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        # If target is in the middle one-third
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)
    
    # Target is not present in the array
    return -1

# Driver code
if __name__ == "__main__":
    # Example sorted array
    arr = [1, 5, 9, 15, 22, 34, 45, 51, 67, 78, 84, 92]
    
    # Element to search for
    target = 22
    
    # Ternary search in the array
    result = ternary_search(arr, 0, len(arr) - 1, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
