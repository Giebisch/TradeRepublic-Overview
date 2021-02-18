import argparse

from .parse_pdfs import parse_pdfs
from .display_value import display_value, get_positions

def main():
    parser = argparse.ArgumentParser()

    # parse all PDFs in folder
    parser.add_argument("--folder", type=str, help=\
        "Specify folder you want to parse the pdfs in")

    # display current depot value
    parser.add_argument("--csv", type=str, help=\
        "Specify the .csv file you want to use")

    args = parser.parse_args()

    if args.folder:
        positions = parse_pdfs(args.folder)
    elif args.csv:
        positions = get_positions(args.csv)
    
    display_value(positions)
