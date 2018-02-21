def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The two given strands must be of the same length.")

    distance = 0
    b = 0
    for a in strand_a:
        if a != strand_b[b]:
            distance += 1
        b += 1

    return distance
