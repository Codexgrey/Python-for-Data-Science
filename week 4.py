def func_one(*names):
    if len(names) < 2:
        print("There's just one argument")
    else:
        print("Hello" + " " + names[1])

func_one("James")


def location(north, east, west, south):
    print(f"I'm currently in the {north}")

location("jigawa", "imo", "ogun", "delta")