def value(colors):
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
    
    return int(str(all_colors.index(colors[0])) + str(all_colors.index(colors[1])))

if __name__ == '__main__':
    print(value(['brown', 'grey', 'white']))