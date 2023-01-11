import csv
import random


class FileReader():
    def __init__(self):
        self.header = []
        self.dataset = []

    def load_dataset(self, file_input, has_header):
        if int(has_header) == 0:
            try:
                with open(file_input, newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        self.dataset.append(row)
            except:
                print('Błąd wczytywania pliku bez nagłówka')
        else:
            try:
                with open(file_input, newline='') as file:
                    reader = csv.reader(file)
                    self.header = next(reader)
                    for row in reader:
                        self.dataset.append(row)
            except:
                print('Błąd wczytywania pliku z nagłówkiem')
        return [self.header, self.dataset]

    def print_header(self):
        if len(self.header) == 0:
            print('Brak etykiet w datasecie')
        else:
            print('Etykiety:\n', self.header)

    def print_data(self, start=0, end=None):
        end = len(self.dataset) if end is None or end > len(self.dataset) else end
        print(self.dataset[start:end])

    def split_dataset_into(self, filereader, train=80, test=10, valid=10):
        try:
            train = int(train)
            test = int(test)
            valid = int(valid)
            random.shuffle(filereader)
        except:
            print('Podano niewlasciwe wartosci')
        if train + test + valid == 100:
            train_set = filereader[0:round(train / 100 * len(filereader))]
            test_set = filereader[round(train / 100 * len(filereader)):round((train + test) / 100 * len(filereader))]
            valid_set = filereader[round((train + test) / 100 * len(filereader)):]

            print(train_set,test_set,valid_set)

        else:
            print('Podano niepoprawne wartosci parametrow')
            raise AttributeError
