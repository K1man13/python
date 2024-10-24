import random

def quickselect(arr, k):
    """
    Finds the Kth largest element in the list using Quickselect algorithm.
    
    :param arr: The list of numbers
    :param k: The Kth largest element to find
    :return: The Kth largest element
    """
    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        # Move pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        
        # Move all elements smaller than the pivot to the left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left, right, k_smallest):
        # Base case: the list contains only one element
        if left == right:
            return arr[left]
        
        # Select a random pivot_index
        pivot_index = random.randint(left, right)
        
        # Find the pivot position in the sorted list
        pivot_index = partition(left, right, pivot_index)
        
        # If the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return arr[k_smallest]
        # If the pivot is too low, go right
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # If the pivot is too high, go left
        else:
            return select(pivot_index + 1, right, k_smallest)

    # We are looking for the (n - k)th smallest element
    return select(0, len(arr) - 1, len(arr) - k)

# Driver code
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    
    result = quickselect(nums, k)
    print(f"The {k}th largest element is {result}.")
