import csv


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
