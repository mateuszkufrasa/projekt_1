from FileReader import FileReader


def main():
    f = FileReader()
    try:
        file_path, if_headers = input(
            'Podaj ścieżkę pliku oraz wartość 1 gdy plik zawiera nagłówek, lub 0 gdy nie zawiera: ').split()
        f.load_dataset(file_path, if_headers)
        f.print_header()
        f.print_data()
    except ValueError:
        print('Błędne argumenty')
    train, test, valid = input(
            'Podaj rpocentowe proporcje zbioru treningowego, testowego i walidacyjnego: ').split()
    f.split_dataset_into(f.dataset, train, test, valid)


main()
