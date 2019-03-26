def czyAnagram():
    s1 = input("wpisz słowo, sprawdzę czy jest anagramem ")
    s2 = input("wpisz drugie słowo ")

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    #print (alist1)
    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    print (matches)

if __name__ == "__main__":
    czyAnagram()

def czyPalindrom():
    s1 = input("wpisz słowo sprawdzę czy jest palindromem ")

    lista1 = list(s1)
    lista2 = list(s1)
    lista2.reverse()
    #print (lista1)
    #print (lista2)
    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if lista1[pos] == lista2[pos]:
            pos = pos + 1
        else:
            matches = False

    print(matches)

if __name__ == "__main__":
    czyPalindrom()

