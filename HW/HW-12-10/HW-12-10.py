def write_to_file(filename, *values):
    try:
        with open(filename, 'w') as f:
            for i in values:
                f.write(str(i) + '\n')
    except OSError as e:
        print(e)


def operation(lam, values) -> float:
    return lam(values)

def geometric_mean(values) -> float:
    if not values:
        return 0
    mult = 1
    for x in values:
        mult *= x
    return mult ** (1 / len(values))


def harmonic_mean(values):
    if not values:
        return 0
    for x in values:
        if x == 0:
            return 0
    reciprocal_sum = 0
    for x in values:
        reciprocal_sum += 1 / x
    return len(values) / reciprocal_sum


def main():
    try:
        results = list()

        values = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

        means = [
            lambda values_l: sum(values_l) / len(values_l),
            lambda values_l: geometric_mean(values_l),
            lambda values_l: sum(values_l) ** 3 / len(values_l)
        ]

        for mean in means:
            results.append(operation(mean, values))

        write_to_file('results.txt', *results , '', f'max: {max(results)}', f'min: {min(results)}')
    except :
        print("error")






if __name__ == '__main__': main()