def part1(input):
    dial = 50
    zero_hits = 0

    for line in input:
        direction, *rest = line
        amount = int("".join(rest))
        if direction == 'L':
            dial = (dial - amount + 100) % 100
        else:
            dial = (dial + amount) % 100

        if dial == 0:
            zero_hits += 1

    return zero_hits

def part2(input):
    dial = 50
    zero_hits = 0

    # print()
    # print()

    for line in input:
        direction, *rest = line
        amount = int("".join(rest))

        zero_hits += (abs(amount) // 100)

        one_turn_amount = amount % 100
        dial_before = dial

        # print('Dial', dial_before, direction, amount, one_turn_amount)
        if direction == 'L':
            dial = (dial - one_turn_amount + 100) % 100
            if dial_before > 0 and dial_before - one_turn_amount <= 0:
                # print('-> hit L')
                zero_hits += 1
        else:
            dial = (dial + one_turn_amount) % 100
            if dial_before < 100 and dial_before + one_turn_amount >= 100:
                # print('-> hit R')
                zero_hits += 1

    # print('-> final', dial_before, dial)

    return zero_hits
