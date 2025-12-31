from itertools import batched

def part1(input):
    invalids_sum = 0
    parsed = input[0].split(',')

    for line in parsed:
        start, end = line.split('-')
        for i in range(int(start), int(end) + 1):
            i_str = str(i)
            first_part = i_str[0:len(i_str) // 2]
            second_part = i_str[len(i_str) // 2:]
            if first_part == second_part:
                invalids_sum += i

    return invalids_sum

def part2(input):
    invalids_sum = 0
    parsed = input[0].split(',')

    for line in parsed:
        start, end = map(int, line.split('-'))
        for i in range(start, end + 1):
            factors = _get_factors(len(str(i)))
            for f in factors:
                parts = ["".join(batch) for batch in batched(str(i), f)]
                if len(set(parts)) == 1 and len(parts) > 1:
                    invalids_sum += i
                    break

    return invalids_sum

def _get_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)      # The divisor
            factors.add(n // i) # The paired factor
    return sorted(list(factors))
