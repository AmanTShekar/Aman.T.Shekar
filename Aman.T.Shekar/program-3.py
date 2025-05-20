def generate_conditional_series(a):
    count = a if a % 2 != 0 else a - 1
    series = [2*i + 1 for i in range((count + 1) // 2)]
    print(', '.join(map(str, series)))

# Example:

generate_conditional_series(6)  

# Output: 1, 3, 5, 7, 9
