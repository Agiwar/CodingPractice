import argparse


def argparse_integer() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--int", type=int)
    return parser.parse_args()


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    
    for _ in range(2, n):
        a, b = b, (a + b)
    
    return b


if __name__ == "__main__":
    args = argparse_integer()
    num_of_stairs = args.int
    num_different_ways = climb_stairs(num_of_stairs)

    # given n = 5, you may get 8
    print(num_different_ways)
