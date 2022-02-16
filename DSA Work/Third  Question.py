def knapsack(capacity, n, weight, values):

    #capacity: will be the maximum capacity of the bag
    #n: will be the number of items acquired
    #weight: will be the weight of items
    #values: will be the values of items
    #:return:

    m = {}
    combined = []
    for c in range(capacity + 1):
        m[(0, c)] = 0

    for i in range(1, n + 1):
        for c in range(capacity + 1):
            if weight[i - 1] <= c:
                m[(i, c)] = max(m[(i-1, c)], values[i-1] + m[(i-1, c-weight[i-1])])

            else:
                m[(i, c)] = m[(i-1, c)]

    print(m[(n, capacity)])
    while n != 0:
        if m[(n, capacity)] != m[(n-1, capacity)]:
            print(f"The package number {n} of the value {values[n - 1]} will weigh {weight[n - 1]} Kgs")
            capacity = capacity - weight[n - 1]

        n -= 1


knapsack(20, 8, [5, 3, 1, 6, 8, 4, 11, 12], [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500])