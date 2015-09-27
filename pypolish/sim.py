def jaccard_index(I, A, B, U):
    U = A + B - I
    res = float(I) / float(U)
    if res < 0 or res > 1:
        raise ValueError("invalid similarity : " + str(res))
    return res
