import argparse
import pyperclip
from random import randint, sample
from string import digits, punctuation, ascii_lowercase, ascii_uppercase


def get_char(seq: str) -> str:
    return seq[randint(0, len(seq)-1)]


def make_password(length: int) -> str:
    index = 0
    password = []
    ascii_chars = [
        digits,
        punctuation,
        ascii_lowercase,
        ascii_uppercase
    ]
    for _ in range(length):
        if index == len(ascii_chars):
            index = 0
            ascii_chars = sample(ascii_chars, k=len(ascii_chars))
        password.append(get_char(ascii_chars[index]))
        index += 1

    return r''.join(sample(password, k=len(password)))


def main():
    parser = argparse.ArgumentParser(
        description='Random Password Generator',
    )
    parser.add_argument('-c', '--copy',
                        help='copy password to clipboard', action='store_true')
    parser.add_argument('-H', '--hide',
                        help='do not print password on console', action='store_true')
    parser.add_argument('-l', '--length',
                        help='password length (default 16)', type=int, default=16)

    args= parser.parse_args()

    password = make_password(args.length)
    if not args.hide:
        print(password)
    if args.copy:
        pyperclip.copy(password)


if __name__ == '__main__':
    main()
