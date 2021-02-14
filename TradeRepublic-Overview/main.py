import argparse

from parse_pdfs import parse_pdfs
from display_value import display_value

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # parse all PDFs in folder
    parser.add_argument("--parse", type=str)

    # display current depot value
    parser.add_argument("--value")

    args = parser.parse_args()

    if args.parse:
        parse_pdfs("test")
    elif args.value:
        display_value()
