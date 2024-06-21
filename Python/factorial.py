import argparse


# Recursion is when a function calls itself with a smaller output,
# and it will be executed until a base case is reached (can be either for or while loop).

# a recursion implementation of n! (n-factorial) calculation
# n! = n * (n - 1) * (n - 2) * ... * 1
#    = n * (n - 1)!


def argparse_integer() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--int", type=int)
    args = parser.parse_args()
    return args


def factorial(n: int) -> int:
    # base case: n = 1 or 0
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)


if __name__ == "__main__":
    args = argparse_integer()
    n = args.int
    n_factorial = factorial(n)

    # given n = 5, you get 120
    print(n_factorial)
