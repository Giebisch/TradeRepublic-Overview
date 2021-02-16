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

def display_value(folder):
    positions = get_positions(folder)
    values = get_current_values(positions)
    # print_formatted_value(value, "|")
    print(values)

    while True:
        time.sleep(10 * 60) # 10 minutes
        current_values = get_current_values(positions)

    #     if current_value > value:
    #         print_formatted_value(current_value, "+")
    #     elif current_value < value:
    #         print_formatted_value(current_value, "-")
        # values = current_value
        
        print(current_values)
        