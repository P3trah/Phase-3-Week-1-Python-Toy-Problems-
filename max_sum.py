def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def solution(A):
    digit_sum_dict = {} 
    max_sum = -1

    for num in A:
        current_sum = digit_sum(num)

        if current_sum in digit_sum_dict:
            max_sum = max(max_sum, num + digit_sum_dict[current_sum])
    
        digit_sum_dict[current_sum] = max(digit_sum_dict.get(current_sum, 0), num)

    return max_sum

# Examples:
A1 = [51, 71, 17, 42]
result1 = solution(A1)
print(f"Example 1: {result1}")

A2 = [42, 33, 60]
result2 = solution(A2)
print(f"Example 2: {result2}")

A3 = [51, 32, 43]
result3 = solution(A3)
print(f"Example 3: {result3}")
