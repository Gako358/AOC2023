class Game:
    def __init__(self, id, red, green, blue):
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue

    def power(self):
        return self.red * self.green * self.blue


games = []
with open("./../../resources/day2.txt", "r") as file:
    for line in file:
        id, *turns = line.strip().split(": ")
        id = int(id.split(" ")[1])
        red = green = blue = 0
        for turn in turns[0].split("; "):
            for cube in turn.split(", "):
                count, color = cube.split(" ")
                if color == "red":
                    red = max(red, int(count))
                elif color == "green":
                    green = max(green, int(count))
                elif color == "blue":
                    blue = max(blue, int(count))
        games.append(Game(id, red, green, blue))

possible_games = list(
    filter(lambda game: game.red <= 12 and game.green <= 13 and game.blue <= 14, games)
)
sum_of_ids = sum(game.id for game in possible_games)
print(f"Part One: {sum_of_ids}")

total_power = sum(game.power() for game in games)
print(f"Part Two: {total_power}")
