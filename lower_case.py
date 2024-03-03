def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern_length = len(alphabet)
    num_full_patterns = N // pattern_length
    remaining_chars = N % pattern_length
    
    result = alphabet * num_full_patterns
    
    if remaining_chars > 0:
        result += alphabet[:remaining_chars]
    
    return result

# Examples:
print("Example 1:", solution(3))
print("Example 2:", solution(5))
print("Example 3:", solution(30))
