import argparse


# Fibonacci sequence is a sequence that the n-th number is coming from (n-th - 1) + (n-th - 2)
# And it's starting from F(0) = 0, F(1) = 1


def argparse_integer() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--int", type=int)
    return parser.parse_args()


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect input.")
    elif n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect input.")
    
    if n == 0:
        return n
    
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, (a + b)
    
    return b


if __name__ == "__main__":
    args = argparse_integer()
    n = args.int
    n_th_fibonacci_rec = fibonacci_recursive(n)
    n_th_fibonacci_itr = fibonacci_iterative(n)

    # given n = 5, you may get 5; n = 10, get 55
    print(f"{n_th_fibonacci_rec} = {n_th_fibonacci_itr}")
