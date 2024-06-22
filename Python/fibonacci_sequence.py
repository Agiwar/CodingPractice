import argparse


# Fibonacci sequence is a sequence that the n-th number is coming from (n-th - 1) + (n-th - 2)
# And it's starting from F(0) = 0, F(1) = 1


def argparse_integer() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--int", type=int)
    args = parser.parse_args()
    return args


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect input.")
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    args = argparse_integer()
    n = args.int
    n_th_fibonacci = fibonacci(n)

    # given n = 5, you may get 5; n = 10, get 55
    print(n_th_fibonacci)
