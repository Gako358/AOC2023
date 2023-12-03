import numpy


class EngineSchematic:
    TEST_SCHEMATIC = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    def __init__(self, input_data, test_result=None):
        if isinstance(input_data, str):
            with open(input_data, "r") as file:
                self.schematic = [list(row.strip()) for row in file.readlines()]
        elif isinstance(input_data, list):
            self.schematic = [list(row) for row in input_data]
        self.searched = []
        self.test_result = test_result

    def get_full_number(self, x, y):
        y_min, y_max = y, y
        while y_min - 1 >= 0 and self.schematic[x][y_min - 1].isdigit():
            y_min -= 1
        while y_max < len(self.schematic[x]) and self.schematic[x][y_max].isdigit():
            y_max += 1

        number = "0"
        if [x, y_min, y_max] not in self.searched:
            number = "".join(self.schematic[x][y_min:y_max])
            self.searched.append([x, y_min, y_max])

        return int(number)

    def adjacent_numbers(self, i, j):
        numbers = []
        for x in range(-1, 1 + 1):
            for y in range(-1, 1 + 1):
                if self.schematic[i + x][j + y].isdigit():
                    number = self.get_full_number(i + x, j + y)
                    if number != 0:
                        numbers.append(number)

        return numbers

    def solve(self, gears=False):
        self.searched = []
        parts = []
        for i in range(0, len(self.schematic)):
            for j in range(0, len(self.schematic[i])):
                if not self.schematic[i][j].isdigit() and self.schematic[i][j] != ".":
                    parts.append([self.schematic[i][j], self.adjacent_numbers(i, j)])

        if gears:
            return sum(
                [
                    numpy.prod(part[1])
                    for part in parts
                    if part[0] == "*" and len(part[1]) == 2
                ]
            )
        else:
            return sum([sum(part[1]) for part in parts])


if __name__ == "__main__":
    engine = EngineSchematic("./../../resources/day3.txt")
    print(engine.solve())

    print(engine.solve(gears=True))

    engine_test = EngineSchematic(EngineSchematic.TEST_SCHEMATIC, test_result=4361)
    assert engine_test.solve() == engine_test.test_result, "Test case failed!"
    print("Test case passed!")

    engine_test2 = EngineSchematic(EngineSchematic.TEST_SCHEMATIC, test_result=467835)
    assert engine_test2.solve(gears=True) == engine_test2.test_result, "Test case failed!"
    print("Test case passed!")