from colorama import Fore, Style

# Define colors
colors = {
    'R': {"upper": "RED", "lower": "Red"},
    'B': {"upper": "BLUE", "lower": "Blue"},
    'C': {"upper": "CYAN", "lower": "Cyan"},
    'Y': {"upper": "YELLOW", "lower": "Yellow"},
    'G': {"upper": "GREEN", "lower": "Green"},
    'M': {"upper": "MAGENTA", "lower": "Magenta"}
}

# Print color menu
for key, value in colors.items():
    print(Fore.WHITE + f"{key}. " + getattr(Fore, value["upper"]) + value["lower"])

# Get user input
chosen_color_key = input("\nChoose a color: ").upper()

# Check if the chosen color is valid
if chosen_color_key in colors:
    chosen_color = colors[chosen_color_key]
    print(f"\nUpper case: {chosen_color['upper']}")
    print(f"Lower case: {chosen_color['lower']}")

    with open("chosen_color.txt", "w") as file:
        file.write(chosen_color['upper'])
        print(f"\n'{chosen_color['upper']}' has been written to 'chosen_color.txt'.")
else:
    print("Invalid color choice. Please choose a valid color.")

# Main script to run the color menu and write the chosen color to a file
