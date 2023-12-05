class Garden:
    def __init__(self, seeds, maps):
        self.seeds = seeds
        self.maps = maps

    def convert(self, source, conversion_map):
        for src_range, dest in conversion_map:
            if src_range[0] <= source <= src_range[1]:
                print(f"Converting {source} to {dest} using {src_range}")
                return dest
        return source  

    def find_lowest_location(self):
        lowest_location = float("inf")
        for seed in self.seeds:
            number = seed
            for conversion_map in self.maps:
                converted = self.convert(number, conversion_map)
                if converted is not None:
                    number = converted
                else:
                    break
            lowest_location = min(lowest_location, number)
            print(f"Lowest location so far: {lowest_location}")
        return lowest_location

    @staticmethod
    def read_from_file(filename):
        with open(filename, "r") as file:
            file.readline()  # skip the 'seeds:' line
            seeds = list(map(int, file.readline().split()))

            maps = []
            for _ in range(7):
                file.readline()  # skip the map title line
                conversion_map = []
                line = file.readline()
                while line.strip():  # read until an empty line
                    src1, src2, dest = map(int, line.split())
                    conversion_map.append(
                        ((src1, src2), dest)
                    )  # create a range with two numbers
                    line = file.readline()
                maps.append(conversion_map)
            return Garden(seeds, maps)

    @staticmethod
    def test_garden():
        garden = Garden(
            [10],
            [
                [((1, 20), 5)],
                [((1, 10), 8)],
                [((1, 5), 10)],
                [((6, 10), 1)],
                [((1, 5), 6)],
                [((6, 10), 3)],
                [((1, 5), 9)],
            ],
        )
        assert garden.find_lowest_location() == 9


def main():
    Garden.test_garden()
    garden = Garden.read_from_file("./../../resources/day5.txt")
    print(garden.find_lowest_location())


if __name__ == "__main__":
    main()
