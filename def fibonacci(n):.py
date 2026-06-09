def fibonacci_series(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    series = fibonacci_series(n - 1)
    series.append(series[-1] + series[-2])
    return series

print(fibonacci_series(10))