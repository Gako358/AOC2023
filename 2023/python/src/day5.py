import re
from scipy.optimize import minimize

class Garden:
    def __init__(self, seeds, ranges):
        self.seeds = seeds
        self.ranges = ranges

    def process(self, seed):
        for range in self.ranges:
            for dst, src, width in range:
                if src <= seed <= (src + width):
                    seed = seed - src + dst
                    break
        return seed

    def find_lowest_location(self):
        answer = min([self.process(seed) for seed in self.seeds])
        return answer
    
    def test_find_lowest_location(self):
        seeds = [79, 14, 55, 13]
        ranges = [
            [[50, 98, 2], [52, 50, 48]],
            [[81, 79, 1], [14, 14, 1], [57, 55, 1], [13, 13, 1]],
            [[81, 79, 1], [53, 14, 1], [57, 55, 1], [52, 13, 1]],
            [[81, 79, 1], [49, 14, 1], [53, 55, 1], [41, 13, 1]],
            [[74, 79, 1], [42, 14, 1], [46, 55, 1], [34, 13, 1]],
            [[78, 79, 1], [42, 14, 1], [82, 55, 1], [34, 13, 1]],
            [[78, 79, 1], [43, 14, 1], [82, 55, 1], [35, 13, 1]],
            [[82, 79, 1], [43, 14, 1], [86, 55, 1], [35, 13, 1]]
        ]
        garden = Garden(seeds, ranges)
        result = garden.find_lowest_location()
        print(f"find_lowest_location returned: {result}")
        assert result == 35, "Test failed!"
        print("Test passed!")

    def find_lowest_location_part2(self):
        answer = 1 << 31
        for j in range(len(self.seeds) // 2):
            bounds = (self.seeds[2 * j], self.seeds[2 * j] + self.seeds[2 * j + 1])
            res = minimize(self.process, x0=self.seeds[2 * j], bounds=[bounds], method='powell')
            answer = min(answer, res.fun)
        return int(answer)

    @staticmethod
    def read_from_file(filename):
        s = open(filename).read().strip().split("\n\n")
        seeds = [int(x) for x in re.findall("\d+", s[0])]
        ranges = []
        for x in s[1:]:
            y = x.split("\n")
            ranges.append([[int(w) for w in re.findall("\d+", z)] for z in y[1:]])
        return Garden(seeds, ranges)

def main():
    garden = Garden.read_from_file("./../../resources/day5.txt")
    print("Part 1:", garden.find_lowest_location())
    print("Part 2:", garden.find_lowest_location_part2())
    garden.test_find_lowest_location()

if __name__ == "__main__":
    main()