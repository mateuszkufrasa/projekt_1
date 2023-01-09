import csv
import random

from Utilities import Utilities


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
        except:
            print('Podano niewlasciwe wartosci')
        if train + test + valid == 100:
            index_range = list(range(len(filereader)))
            train_indexes = random.sample(index_range, round(train * len(index_range) / 100))  # wybiera liste indeksow dla zespolu treningowego
            train_set = [filereader[x] for x in train_indexes]
            filereader = [filereader[x] for x in train_indexes if x not in filereader]
            index_range = list(range(len(filereader)))
            test_indexes = random.sample(index_range, round(test * len(index_range) / 100))  # wybiera liste indeksow dla zespolu testowego
            test_set = [filereader[x] for x in test_indexes]
            filereader = [filereader[x] for x in test_indexes if x not in filereader]
            index_range = list(range(len(filereader)))
            valid_indexes = random.sample(index_range, round(valid * len(index_range) / 100))  # wybiera liste indeksow dla zespolu testowego
            valid_set = [filereader[x] for x in valid_indexes]
            filereader = [filereader[x] for x in valid_indexes if x not in filereader]
            print(train_set,test_set,valid_set)

        else:
            print('Podano niepoprawne wartosci parametrow')
