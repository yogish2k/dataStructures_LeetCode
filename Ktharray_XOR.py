def m_step_xor(a, m, k):
    n = len(a)

    # the total number of element remain after m operation
    # is n-m so the index that are greater than or equal to
    # n-m in zero-based indexing will be not present
    if k >= n - m:
        return -1

    # considering m<2^18
    for i in range(5):

        # check whether ith bit is on or not in m
        if m & (1 << i):
            m -= (1 << i)

            # as the bit is on
            # Updating index that exist with the relation
            # a[i]=a[i]^a[i+2^j]
            for j in range(n - (1 << i)):
                a[j] = a[j] ^ a[j + (1 << i)]

    # returning the Kth index in updated array after M
    # operation
    return a[k]


a = [1, 4, 5, 6, 7]

m = 2
k = 2

ans = m_step_xor(a, m, k)

print(ans)
