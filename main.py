from dodawanie import dodawanie
from odejmowanie import odejmowanie
from mnozenie import mnozenie
from dzielenie import dzielenie

def main():
    print("Hello, World!")
    # Add more functionality here as needed
    print("This is a simple Python script.")
    print("1 dodawanie")
    print("2 odejmowanie")
    print("3 mnozenie")
    print("4 dzielenie")
    wybor = input("Wybierz operacje: ")
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))

    if wybor == "1":
        print(f"Wynik dodawania: {dodawanie(a, b)}")
    elif wybor == "2":
        print(f"Wynik odejmowania: {odejmowanie(a, b)}")
    elif wybor == "3":
        print(f"Wynik mnozenia: {mnozenie(a, b)}")
    elif wybor == "4":
        print(f"Wynik dzielenia: {dzielenie(a, b)}")
    else:
        print("Nieznana operacja!")

if __name__ == "__main__":
    main()