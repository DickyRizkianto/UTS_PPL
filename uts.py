import os
import sys
import time
import math

# ======== MODE 2: Rainbow Gradient Function ========
def rainbow(i):
    r = int(127 * math.sin(i + 0) + 128)
    g = int(127 * math.sin(i + 2) + 128)
    b = int(127 * math.sin(i + 4) + 128)
    return f"\033[38;2;{r};{g};{b}m"

reset = "\033[0m"


# ======== MODE 1: Animasi Zig-Zag Rainbow Bergerak ========
def mode_animasi():
    colors = [
        "\033[91m", "\033[93m", "\033[92m",
        "\033[96m", "\033[94m", "\033[95m"
    ]

    width = 30
    height = 40
    speed = 0.03

    indent = 0
    direction = 1
    color_index = 0

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            temp_indent = indent
            temp_color = color_index

            for i in range(height):
                color = colors[temp_color]
                print(" " * temp_indent + color + "@@" * 4 + reset)

                temp_indent += direction
                if temp_indent <= 0 or temp_indent >= width:
                    direction *= -1
                temp_color = (temp_color + 1) % len(colors)

            indent += direction
            if indent <= 0 or indent >= width:
                direction *= -1

            color_index = (color_index + 1) % len(colors)

            time.sleep(speed)

    except KeyboardInterrupt:
        print(reset)
        print("\nKembali ke menu...")
        time.sleep(1)


# ======== MODE 2: Zig-Zag Gradient Estetik (Static Art) ========
def mode_gradient_static():
    height = 45
    width = 12
    direction = 1
    indent = 0
    t = 0

    for i in range(height):
        color = rainbow(t)
        print(" " * indent + color + "@@" * 5 + reset)

        indent += direction
        if indent >= width or indent <= 0:
            direction *= -1

        t += 0.4

    print(reset)
    input("\nTekan ENTER untuk kembali ke menu...")


# ======== MENU UTAMA ========
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=== MENU ANIMASI TERMINAL ===")
        print("1. Animasi Zig-Zag Rainbow Bergerak")
        print("2. Zig-Zag Gradient Estetik (Static Art)")
        print("3. Keluar")
        print("==============================")
        pilihan = input("Pilih mode: ")

        if pilihan == "1":
            mode_animasi()
        elif pilihan == "2":
            mode_gradient_static()
        elif pilihan == "3":
            print("Keluar...")
            sys.exit()
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)


# ======== START PROGRAM ========
menu()
