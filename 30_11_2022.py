from typing import Any


def read_imput(nazwa_pliku: str) -> list[str]:
    """Funkcja otwiera zadany plik i zwraca listę zawierającą jako elementy kolejne linijki"""
    try:
        file = open(nazwa_pliku, "r")
        return file.read().splitlines()
    except FileNotFoundError:
        print("Nie ma takiego pliku.")


def pars_line(line: str) -> list[Any]:
    """Funkcja tłumaczy linijkę instrukcji na format potrzebny do dalszego procesowania"""
    split = line.split(" ")
    split[-1] = str_to_tuple(split[-1])
    split[-3] = str_to_tuple(split[-3])
    if len(split) == 4:
        split.pop(2)
        return split
    elif len(split) == 5:
        split = split[1:]
        split.pop(2)
        return split
    else:
        print("Tekst nie jest spodziewanego formatu.")


def str_to_tuple(tekst: str) -> tuple:
    """Funkcja próbuje przekształcić coś co wygląda jak współrzędne (x,y) w formacie tekstowym na tuple zawierającą te współrzędne"""
    try:
        temp = tekst.split(",")
        temp = (int(temp[0]), int(temp[1]))
        return temp
    except ValueError:
        print("Tekst nie przypomina współrzędnych.")
    except IndexError:
        print("Współrzędne nie są rozdzielone przecinkiem.")


def generate_grid(x: int, y: int) -> list[0]:
    """Generuje siatkę zer o zadanej wielkości"""
    grid = []
    for i in range(x):
        grid.append([])
        for ii in range(y):
            grid[i].append(0)
    return grid


def execute(grid: list[list], instructions: list[Any]) -> list[list]:
    """Wykanuje podaną instrukcję na zadanej sitce"""
    for i in range(instructions[1][0], instructions[2][0] + 1):
        for ii in range(instructions[1][1], instructions[2][1] + 1):
            grid[i][ii] = light_switch(grid[i][ii], instructions[0])
    return grid


def light_switch(point: int, instruction: str) -> int:
    """Włączamy, wyłączamy lub przełączamy światełka"""
    if instruction == "on":
        return 1
    elif instruction == "off":
        return 0
    elif instruction == "toggle":
        if point == 1:
            return 0
        else:
            return 1
    else:
        print("Zły parsing.")


def execute_all(instructions: list[Any], grid: list[list]) -> list[list]:
    """Wykonuje listę instrukcji na zadanej siatce"""
    for instruction in instructions:
        grid = execute(grid, instruction)
    return grid


def sum_matrix(matrix: list[list]) -> int:
    """Sumuje macież w formie listy list"""
    return sum([sum(i) for i in zip(*matrix)])


# Wczytujemy plik
lines = read_imput("imput_30_11_2022.txt")
# Tłumaczymy instrukcje na bardziej zrozumiały format
lines = list(map(pars_line, lines))
# generujemy światełka
lights = generate_grid(1000, 1000)
# wykonyjemy instrukcje św. Mikołaja
lights = execute_all(lines, lights)
# wynik ile światełek jest zapalonych
print(sum_matrix(lights))
