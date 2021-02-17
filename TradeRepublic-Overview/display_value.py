import os
from csv import reader, DictReader
import time
import requests

def get_current_values(positions):
    # official ls exchange .csv file
    url = "https://www.ls-x.de/_rpc/json/.lstc/instrument/list/lsxtradestoday"

    ls_download = requests.get(url).text
    iterable = ls_download.split("\n")

    csv = DictReader(iterable, delimiter=";", quotechar='"')
    for line in csv:
        for position in positions:
            if line["isin"] == position["isin"]:
                position["worth"] = float(line["price"].replace(",", ".")) * position["quantity"]

    return positions

def get_positions(folder):
    positions = []
    try:
        with open(os.path.join(folder, "positions.csv")) as infile:
            csv = reader(infile, delimiter=";")
            next(csv)
            for line in csv:
                dic = dict()
                dic["isin"] = line[0]
                dic["quantity"] = float(line[1])
                dic["price"] = float(line[2])
                positions.append(dic)
    except:
        raise Exception("No positions.csv file found, parse your PDFs first.")
    return positions

def print_formatted_values(values, tendency=None):
    sorted_positions = sorted(values, key= lambda x: x["worth"], reverse=True)
    max_length = 0
    for position in sorted_positions:
        isin = position.get("isin")
        worth = f"{position.get('worth'):.2f}"
        if len(worth) > max_length: max_length = len(worth)
        print(f"{isin:20s} {worth.rjust(max_length)}€")

    hline = "_" * (22 + max_length)
    up_arrow = "\u25b2"
    down_arrow = "\u25bc"
    total_worth = str(sum([x["worth"] for x in values])) + "€"

    if tendency == "+":
        total_worth = up_arrow + " " + total_worth
    elif tendency == "-":
        total_worth = down_arrow + " " + total_worth

    print(hline)
    print(total_worth.rjust(len(hline)) + "\n")

def display_value(folder):
    positions = get_positions(folder)
    values = get_current_values(positions)
    worth = sum([x["worth"] for x in values])
    print_formatted_values(values)

    while True:
        time.sleep(10 * 60) # 10 minutes
        current_values = get_current_values(positions)
        current_worth = sum([x["worth"] for x in current_values])

        if current_worth > worth:
            print_formatted_values(current_values, "+")
        elif current_worth < worth:
            print_formatted_values(current_values, "-")

        values = current_values
        worth = current_worth
