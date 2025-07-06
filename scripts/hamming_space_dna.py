def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands must be of equal length.")

    unique_values = list(set(strand_a+strand_b))
    expected_values = ['C', 'A', 'G', 'T']

    outliers = [x for x in unique_values if x not in expected_values]
    if outliers:
        raise ValueError("Strands must only contain C, A, G or T")

    if not unique_values:
        raise ValueError("Strands cannot be empty")

    mismatches = [i for i, j in zip(strand_a, strand_b) if i != j]

    return len(mismatches)