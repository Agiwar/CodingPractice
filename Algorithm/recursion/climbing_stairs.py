import argparse


def argparse_integer() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--int", type=int)
    return parser.parse_args()


def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for _ in range(n - 1):
        one, two = (one + two), one
    
    return one


if __name__ == "__main__":
    args = argparse_integer()
    num_of_stairs = args.int
    num_different_ways = climb_stairs(num_of_stairs)

    # given n = 5, you may get 8
    print(num_different_ways)
