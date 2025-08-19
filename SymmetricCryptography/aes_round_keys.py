from aes_structure import matrix2bytes


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    res = []
    for r1,r2 in zip(s, k):
        res.append([x^y for x,y in zip(r1, r2)])
    return res


if __name__ == '__main__':
    state = add_round_key(state, round_key)
    print(matrix2bytes(state))
