def generate_series(a):
    series = [2*i + 1 for i in range(a)]
    print(', '.join(map(str, series)))

# Example:
generate_series(4)  # Output: 1, 3, 5, 7
