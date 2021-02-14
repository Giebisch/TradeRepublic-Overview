def display_value():
    positions = get_positions()
    value = get_current_value(positions)
    print_formatted_value(value, "|")

    while True:
        current_value = get_current_value(positions)

        if current_value > value:
            print_formatted_value(current_value, "+")
        elif current_value < value:
            print_formatted_value(current_value, "-")
        
        value = current_value
        