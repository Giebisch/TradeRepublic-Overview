import os
from csv import reader

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
    value = get_current_value(positions)
    print_formatted_value(value, "|")

    while True:
        current_value = get_current_value(positions)

        if current_value > value:
            print_formatted_value(current_value, "+")
        elif current_value < value:
            print_formatted_value(current_value, "-")
        
        value = current_value
        