import argparse


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_string", type=str, nargs="?")  # nargs='?': This will make argparse treat the entire input as a single string, allowing you to pass the input in quotes.
    return parser.parse_args()


def is_valid_parentheses(s: str) -> bool:
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    if s[0] not in pairs.keys() or len(s) == 1:
        return False

    stack = []
    for char in s:
        if char in pairs:
            stack.append(char)
        elif stack and pairs[stack[-1]] == char:
            stack.pop()
        else:
            return False
        
    return not stack


if __name__ == "__main__":
    args = argparse_list()
    given_str = args.given_string.replace(" ", "")  # strip spaces from the input string before parsing
    is_valid = is_valid_parentheses(given_str)

    # given ( ) [ ] { } , you may get True
    # given ( ( , you may get False
    # given ( ) { } } { , you may get False
    print(is_valid)
