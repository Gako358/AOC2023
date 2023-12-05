class ScratchCard:
    def __init__(self, winning_numbers, your_numbers):
        self.winning_numbers = set(map(int, filter(None, winning_numbers.split(" "))))
        self.your_numbers = set(map(int, filter(None, your_numbers.split(" "))))

    def calculate_points(self):
        matches = self.winning_numbers & self.your_numbers
        return (lambda x: 2 ** (len(x) - 1) if x else 0)(matches)

    def calculate_won_cards(self):
        matches = self.winning_numbers & self.your_numbers
        return len(matches)

    @staticmethod
    def read_cards_from_file(filename):
        with open(filename, "r") as file:
            cards = [
                ScratchCard(*numbers.partition(":")[2].strip().split("|"))
                for numbers in file
                if numbers.startswith("Card")
            ]
        return cards

    @staticmethod
    def calculate_total_cards(cards):
        num_copies = [1] * len(cards)
        for i in range(len(cards)):
            won_cards = cards[i].calculate_won_cards()
            for j in range(i + 1, min(i + 1 + won_cards, len(cards))):
                num_copies[j] += num_copies[i]
        return sum(num_copies)

    @staticmethod
    def test_scratch_card():
        test_cards = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        cards = [
            ScratchCard(*line.partition(":")[2].strip().split("|"))
            for line in test_cards
        ]
        total_points = sum(card.calculate_points() for card in cards)
        assert total_points == 13, f"Expected 13, but got {total_points}"
        print("Test passed.")


def main():
    ScratchCard.test_scratch_card()
    cards = ScratchCard.read_cards_from_file("./../../resources/day4.txt")
    total_points = sum(card.calculate_points() for card in cards)
    print(f"Total points: {total_points}")
    total_cards = ScratchCard.calculate_total_cards(cards)
    print(f"Total cards: {total_cards}")


if __name__ == "__main__":
    main()
