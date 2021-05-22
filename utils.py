def abs_error(a, b):
    n = len(a)
    c = [None for _ in range(n)]
    for i in range(n):
        c[i] = abs(a[i] - b[i])
    return c