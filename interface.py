def line(size=40):
    return "-" * size


def header(txt):
    print(line())
    print(txt.center(len(line())))
    print(line())


def menu(data):
    header("MAIN MENU")
    c = 1
    for item in data:
        print(f"{c} - {item} ")
        c += 1
    print(line())
    option = readinteger("Choose an option:")
    return option


def readinteger(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERROR! Insert a valid integer number\033[m.")
            continue
        except KeyboardInterrupt:
            print(f"\n\033[0;31mThe user preferred not to inform this data.\033[m")
            return 0
        else:
            return n
