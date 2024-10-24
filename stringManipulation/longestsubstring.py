def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last position of each character
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        current_char = s[end]

        # If the character is already in the map and its index is within the current window
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1  # Move the start to the right of the last occurrence

        # Update the last index of the character
        char_index_map[current_char] = end

        # Calculate the length of the current substring and update max_length
        max_length = max(max_length, end - start + 1)

    return max_length

# Driver code
if __name__ == "__main__":
    # Example string
    s = "abcabcbb"
    
    # Find the length of the longest substring without repeating characters
    result = length_of_longest_substring(s)
    
    print(f"The length of the longest substring without repeating characters is {result}.")
