COLOUR_NAME_TO_HEX = {
    "AbsoluteZero":    "#0048ba",
    "AcidGreen":       "#b0bf1a",
    "AliceBlue":       "#f0f8ff",
    "AlizarinCrimson": "#e32636",
    "Amaranth":        "#e52b50",
    "Amber":           "#ffbf00",
    "Amethyst":        "#9966cc",
    "AntiqueWhite":    "#faebd7",
    "Aqua":            "#00ffff",
    "Aquamarine":      "#7fffd4"
}

colour_name = input("Enter a colour name (or blank to quit): ").title()
while colour_name !="":
    if colour_name in COLOUR_NAME_TO_HEX:
        print(f"{colour_name} is {COLOUR_NAME_TO_HEX[colour_name]}")
    else:
        print(f"{colour_name} is not a valid colour.")
    colour_name = input("Enter a colour name (or blank to quit): ").title()
