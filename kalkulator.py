from typing import Any


def main():
    wybor = "t"
    while wybor == "t":
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
        liczba_1 = float(input())
        dzialanie = str(input())
        liczba_2 = float(input())


        suma = 0
        roznica = 0
        iloczyn = 0
        iloraz = 0
        reszta = 0


        if dzialanie == "+":
            suma = liczba_1 + liczba_2
            print ( "Twój wynik to: " + str(suma))
            wybor = str(input("Chcesz wykonać kolejne działanie? Wpisz literę t lub n: "))
        elif dzialanie == "-":
            roznica = liczba_1 - liczba_2
            print ("Twój wynik to: " + str(roznica))
            wybor = input("Chcesz wykonać kolejne działanie? Wpisz literę t lub n: ")
        elif dzialanie == "*":
            iloczyn = liczba_1 * liczba_2
            print("Twój wynik to: " + str(iloczyn))
            wybor = input("Chcesz wykonać kolejne działanie? Wpisz literę t lub n: ")
        elif dzialanie == "/":
            if liczba_2 == 0:
                print("nie dziel przez zero")
            else:
                iloraz = liczba_1 / liczba_2
                print("Twój wynik to: " + str(iloraz))
            wybor = input("Chcesz wykonać kolejne działanie? Wpisz literę t lub n: ")
        elif dzialanie == "%":
            reszta = liczba_1 % liczba_2
            print("Twój wynik to: " + str(reszta))
            wybor = input("Chcesz wykonać kolejne działanie? Wpisz literę t lub n: ")



    print ("koniec programu")

if __name__ == "__main__":
    main()