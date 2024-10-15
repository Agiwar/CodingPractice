import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_operations", type=str, nargs="+")
    return parser.parse_args()


def cal_points(operations: List[str]) -> int:
    record = []

    for operation in operations:
        if operation == "D":
            record.append(record[-1] * 2)
        elif operation == "C":
            record.pop()
        elif operation == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(operation))
    
    return sum(record)


if __name__ == "__main__":
    args = argparse_list()
    given_operations = args.given_operations
    baseball_game_record = cal_points(given_operations)

    # given "5" "2" "C" "D" "+", you may get 30
    print(baseball_game_record)
