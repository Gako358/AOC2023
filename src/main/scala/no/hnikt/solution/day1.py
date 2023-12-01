class Calibration:
    num_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    @staticmethod
    def solve(data, with_spelled_nums=False):
        calibration_vals = []
        for line in data:
            first_pos = 1e6
            last_pos = -1
            first = last = ""

            for pos, char in enumerate(line): 
                if char.isdigit():
                    first_pos = pos
                    first = char
                    break

            for pos, char in enumerate(line[::-1]):
                if char.isdigit():
                    last_pos = (
                        len(line) - pos - 1
                    ) 
                    last = char
                    break

            if with_spelled_nums:
                for num_word in Calibration.num_words:
                    pos = line.find(num_word)
                    if 0 <= pos < first_pos:
                        first_pos = pos
                        first = str(
                            Calibration.num_words[num_word]
                        ) 

                    pos = line.rfind(num_word)
                    if pos > last_pos:
                        last_pos = pos
                        last = str(Calibration.num_words[num_word])

            calibration_vals.append(int(first + last))

        return sum(calibration_vals)


if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        input_data = f.read().splitlines()

    soln = Calibration.solve(input_data, with_spelled_nums=True)

    print(f"Solution: {soln}")
