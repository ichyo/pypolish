def jaccard_index(I, A, B, U):
    U = A + B - I
    return float(I) / float(U)
