def rec_sum(n):
    # write the insides here!
    if n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)
