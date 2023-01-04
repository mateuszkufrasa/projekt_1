from FileReader import FileReader


def main():
    try:
        file_path, if_headers = input(
            'Podaj ścieżkę pliku oraz wartość 1 gdy plik zawiera nagłówek, lub 0 gdy nie zawiera: ').split()
        f = FileReader()
        f.load_dataset(file_path, if_headers)
        f.print_header()
        f.print_data()
    except ValueError:
        print('Błędne argumenty')


main()
