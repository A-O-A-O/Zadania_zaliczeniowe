from typing import Any


class BestCristmasLightsEver:
    def __init__(self, file_name, x, y):
        self.file_name = file_name
        self.x = x
        self.y = y
        self._lines = None
        self._grid = None

    def read_imput(self):
        """Funkcja otwiera zadany plik i zwraca listę zawierającą jako elementy kolejne linijki"""
        try:
            file = open(self.file_name, "r")
            self._lines = file.read().splitlines()
        except FileNotFoundError:
            print("Nie ma takiego pliku.")

    def pars_line(self, line: str) -> list[Any]:
        """Funkcja tłumaczy linijkę instrukcji na format potrzebny do dalszego procesowania"""
        split = line.split(" ")
        split[-1] = self.str_to_tuple(split[-1])
        split[-3] = self.str_to_tuple(split[-3])
        if len(split) == 4:
            split.pop(2)
            return split
        elif len(split) == 5:
            split = split[1:]
            split.pop(2)
            return split
        else:
            print("Tekst nie jest spodziewanego formatu.")

    def pars_lines(self):
        self._lines = list(map(self.pars_line, self._lines))

    def str_to_tuple(self, tekst: str) -> tuple:
        """Funkcja próbuje przekształcić coś co wygląda jak współrzędne (x,y) w formacie tekstowym na tuple zawierającą te współrzędne"""
        try:
            temp = tekst.split(",")
            temp = (int(temp[0]), int(temp[1]))
            return temp
        except ValueError:
            print("Tekst nie przypomina współrzędnych.")
        except IndexError:
            print("Współrzędne nie są rozdzielone przecinkiem.")

    def generate_grid(self):
        """Generuje siatkę zer o zadanej wielkości"""
        grid = []
        for i in range(self.x):
            grid.append([])
            for ii in range(self.y):
                grid[i].append(0)
        self._grid = grid

    def execute(self, instructions: list[Any]):
        """Wykanuje podaną instrukcję na zadanej sitce"""
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for ii in range(instructions[1][1], instructions[2][1] + 1):
                self._grid[i][ii] = self.light_switch(self._grid[i][ii], instructions[0])

    def light_switch(self, point: int, instruction: str) -> int:
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

    def execute_all(self):
        """Wykonuje listę instrukcji na zadanej siatce"""
        for instruction in self._lines:
            self.execute(instruction)

    def sum_matrix(self) -> int:
        """Sumuje macież w formie listy list"""
        return sum([sum(i) for i in zip(*self._grid)])

    def analyze(self):
        self.read_imput()
        self.pars_lines()
        self.generate_grid()
        self.execute_all()
        print(self.sum_matrix())


myLights = BestCristmasLightsEver("imput_30_11_2022.txt", 1000, 1000)
myLights.analyze()
