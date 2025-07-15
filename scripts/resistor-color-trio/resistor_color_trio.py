def label(colors):
    all_colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    
    value = int(str(all_colors.index(colors[0])) + str(all_colors.index(colors[1])) + all_colors.index(colors[2]) * '0')
    
    prefixes = {
        1: "",
        1000: "kilo",
        1000000: "mega",
        1000000000: "giga"
    }

    for prefix_value, prefix in reversed(prefixes.items()):
        if value == 0:
            return "0 ohms"
        elif value >= prefix_value:
            return str(int(value / prefix_value)) + " " + prefix + "ohms"


if __name__ == "__main__":
    print(label(["black", "black", "black"]))