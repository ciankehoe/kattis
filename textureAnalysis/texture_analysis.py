# need to complete / tweak --> not passing all tests

texture = input()

line_number = 1
while texture != "END":
    pixels = set(texture.strip().split("."))
    gaps = set(texture.strip().split("*"))

    pixels -= {""}
    gaps -= {""}

    if (len(pixels) <= 1) and (len(gaps) <= 1):
        print(line_number, "EVEN")
    else:
        print(line_number, "NOT EVEN")

    line_number += 1
    texture = input()
