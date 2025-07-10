def colors():
    return [
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

def color_code(color):
    return colors().index(color)


if __name__ == "__main__":
    print(color_code("violet"))