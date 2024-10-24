def is_match(s: str, p: str) -> bool:
    # Initialize a DP table with False values
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, etc. when matching an empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Iterate through the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            # If characters match or pattern has '.', it depends on the previous state
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            # If the pattern contains '*', we have two cases:
            elif p[j - 1] == '*':
                # Consider zero occurrence of the character before '*'
                dp[i][j] = dp[i][j - 2]
                
                # Consider one or more occurrences of the character before '*'
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[len(s)][len(p)]

# Driver code
if __name__ == "__main__":
    # Example strings and patterns
    s = "aab"
    p = "c*a*b"
    
    # Perform regex matching
    result = is_match(s, p)
    
    if result:
        print(f"The string '{s}' matches the pattern '{p}'.")
    else:
        print(f"The string '{s}' does not match the pattern '{p}'.")
