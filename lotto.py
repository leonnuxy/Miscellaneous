# A code that predicts the winning number for the Western Max Lottery

class Lotto:
    def __init__(self):
        self.numbers = []
        self.winning_number = []
        self.winning_numbers = []
        self.winning_numbers_count = 0
        self.winning_numbers_count_list = []
        self.winning_numbers_count_list_index = 0
        self.winning_numbers_count_list_index_list = []

    def generate_winning_numbers(self):
        for i in range(1, 91):
            self.winning_number.append(i)
        self.winning_number.sort()

    def generate_numbers(self):
        for i in range(1, 91):
            self.numbers.append(i)
        self.numbers.sort()

    def generate_winning_numbers_count(self):
        for i in range(1, 91):
            self.winning_numbers_count += 1

    def generate_winning_numbers_count_list(self):
        for i in range(1, 91):
            self.winning_numbers_count_list.append(self.winning_numbers_count)

    def generate_winning_numbers_count_list_index(self):
        for i in range(1, 91):
            self.winning_numbers_count_list_index += 1

    def generate_winning_numbers_count_list_index_list(self):
        for i in range(1, 91):
            self.winning_numbers_count_list_index_list.append(self.winning_numbers_count_list_index)
