def Q2():
    n, m = input().split()
    edges = []
    m = int(m)
    for i in range(m):
        x, y = input().split()
        edges.append((x, y))
    
    white = []
    black = []
    for i,j in edges:
        if not white.__contains__(i) and not white.__contains__(j) and not black.__contains__(i) and not black.__contains__(j):
            white.append(i)
            black.append(j)
        if white.__contains__(i) and not black.__contains__(j) and not white.__contains__(j):
            black.append(j)
        if black.__contains__(i) and not white.__contains__(j) and not black.__contains__(j):
            white.append(j)
        if white.__contains__(j) and not black.__contains__(i) and not white.__contains__(i):
            black.append(i)
        if black.__contains__(j) and not white.__contains__(i) and not black.__contains__(i):
            white.append(i)

        if white.__contains__(i) and white.__contains__(j):
            return  0
        if black.__contains__(i) and black.__contains__(j):
            return 0

    return 1

print(Q2())