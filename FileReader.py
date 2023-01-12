import csv
import random


class FileReader():
    def __init__(self):
        self.header = []
        self.dataset = []
        self.vals_set = set()

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
        self.dataset = list(filter(None, self.dataset))  # usuwa pusty wiersz
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
            valid_set = filereader[round((train + test) / 100 * len(filereader)):round(
                (train + test + valid) / 100 * len(filereader))]
            print(
                f'Zbior treningowy: {len(train_set)} elementow.\nZbior testowy: {len(test_set)} elementow.\nZbior walidacyjny: {len(valid_set)} elementow.')
            return train_set, test_set, valid_set

        else:
            print('Podano niepoprawne wartosci parametrow')
            raise AttributeError

    def count_decision_class(self):
        for i in self.dataset:
            self.vals_set.add(i[4])
        print(f'Liczba klas decyzyjnych: {len(self.vals_set)}.')
        for el in self.vals_set:
            count = 0
            for i in self.dataset:
                if i[4] == el:
                    count += 1
                else:
                    pass
            print(f'Klasa {el}: {count} elementów.')

    def print_elements_for(self, class_name):
        if class_name.strip() in self.vals_set:
            for i in self.dataset:
                if i[4] == class_name:
                    print(i)
                else:
                    pass
        else:
            print('Podano złą nazwę klasy')

    # TODO: poprawic zapis do pliku csv
    def write_to_csv(self):
        print('Zapis do pliku csv...')
        with open("export.csv", 'w', newline='') as of:
            write = csv.writer(of)
            if len(self.header) > 0:
                write.writerow(self.header)
            else:
                pass
            write.writerows(self.dataset)
        print('Zapisano do pliku csv.')
