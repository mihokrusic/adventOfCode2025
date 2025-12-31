def part1(input):
    joltage_sum = 0

    for line in input:
        indices = []
        indices.append(_get_largest(line, 0, len(line) - 1))
        indices.append(_get_largest(line, indices[0] + 1, len(line)))

        joltage_sum += int(line[indices[0]] + line[indices[1]])

    return joltage_sum

def part2(input):
    joltage_sum = 0

    for line in input:
        indices = []
        indices.append(_get_largest(line, 0, len(line) - 11))
        indices.append(_get_largest(line, indices[0] + 1, len(line) - 10))
        indices.append(_get_largest(line, indices[1] + 1, len(line) - 9))
        indices.append(_get_largest(line, indices[2] + 1, len(line) - 8))
        indices.append(_get_largest(line, indices[3] + 1, len(line) - 7))
        indices.append(_get_largest(line, indices[4] + 1, len(line) - 6))
        indices.append(_get_largest(line, indices[5] + 1, len(line) - 5))
        indices.append(_get_largest(line, indices[6] + 1, len(line) - 4))
        indices.append(_get_largest(line, indices[7] + 1, len(line) - 3))
        indices.append(_get_largest(line, indices[8] + 1, len(line) - 2))
        indices.append(_get_largest(line, indices[9] + 1, len(line) - 1))
        indices.append(_get_largest(line, indices[10] + 1, len(line)))

        joltage = int("".join(map(lambda x: line[x], indices)))
        joltage_sum += joltage

    return joltage_sum

def _get_largest(line, start, end):
    largest_ix = None

    for ix in range(start, end):
        if ix == start:
            largest_ix = ix
        else:
            if line[ix] > line[largest_ix]:
                largest_ix = ix

    return largest_ix
