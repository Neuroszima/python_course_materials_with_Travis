

"""
pierwsze kroki w zmiennych

"""

if __name__ == '__main__':
    '''
    a co jeżeli chcielibyśmy wpisać wartość tylko taką jaką chcemy, a jeszcze 
    jej nie znamy przed uruchomieniem programu?

    w takich przypadkach, przydatna okazuje się funkcja "input"
    '''

    # a = input('podaj a: ')
    # b = input('podaj b: ')

    # print(a + b)

    '''
    dlaczego dodało 3 + 7 i wyszło 37?

    nasz skrypt dodał te dwie zmienne tak jakby były one tekstem

    trzeba skonwertować dane z klawiatury na typ liczbowy, np. "int"
    '''

    # a = int(input('podaj a: '))
    # b = int(input('podaj b: '))

    # print(a + b)

    '''
    możemy definiować różne typy zmiennych, np. 
      łańcuch znaków              (string)
      liczbę całkowitą            (integer)
      wartość prawda/fałsz        (boolean)
      liczbę zmiennoprzecinkową   (float)
    '''

    i = 4
    s = "5"
    b = True
    f = .0

    '''
    możemy sprawdzać typ zmiennej stosując funkcję "type" albo "isinstance"

    w ten sposób możemy sprawdzić czy zmienne odpowiadają temu typowi który chcemy:
    '''

    print(isinstance(i, int))
    print(type(b))
    print(isinstance(b, bool))
    print(type(f))

    if isinstance(b, bool):
        print("działam poprawnie")
    else:
        print("podałeś złe dane, spróbuj jeszcze raz")

    print(type(f) == float)
    print(type(f))
    print(type(float))
    print(float)

    if type(f) == float:
        c = 15. + f
        print(c)
    else:
        print("incorrect data type")

    '''
    co się stanie gdy to do siebie dodamy? czy kolejność ma znaczenie?
    '''

    # print(a + b)
    # print(b + a)

    '''
    nie możemy dodać do siebie tych zmiennych od razu, musimy je przekonwertować na typ który umożliwia nam ich dodawanie
    czyli na typ wspólny dla obu zmiennych (np. obie typu string, obie typu integer itp)
    
    dobra a co jeżeli byśmy chcieli pomnóżyć przez coś tekst?
    '''

    print("AAAAAAAAAA" * 10)

    '''
    zapisywanie danych do pliku

    jest możliwych kilka metod zapisu, najprostszą z nich jest otwarcie już istniejącego pliku i zapisanie do niego
    informacji

    plik otwieramy za pomocą wbudowanej funkcji open, w nawiasie podając nazwę pliku, oraz przekazując go do zmiennej

    mówimy tu o tak zwanym "strumieniu danych" który przypisujemy do zmiennej "file" zaznaczając, że chodzi tu o
    strumień danych zapisywanych do pliku

    następnie odwołujemy się do pliku, po kropce wywołując wewnętrzną funkcję "write" w nawiasie której podajemy dane

    dane muszą mieć format tekstowy; po zapisie zamykamy strumień wywołując wewnętrzną funkcję "close()"
    '''

    a = 5

    file = open('new_file.txt', 'w')
    file.write(str(a))
    file.close()

    '''
    aby nie trzeba było zamykać pliku samemu oraz przypisywać strumienia do zmiennej, możemy użyć również klauzuli

    "
        with (tutaj coś) as (tutaj nazwa, na jaką chcemy przechrzcić nasze coś):
            instrukcje...
    "

    korzystamy tutaj z tzw. "context manager'a"

    CM pozwala nam, w ramach operowania na danej klasie obiektu wykonać pewne funkcje, które wymagane byłyby zawsze

    w przypadku zwykłego otwarcia strumienia danych do pliku są to dwie rzeczy:
        przypisanie strumienia do zmiennej
            oraz
        po zakończonych opearacjach zamknięcie strumienia

    taką konstrukcję można wykorzystać wszędzie, np. przy połączeniach z bazą danych, gdzie w wielu 
    miejscach w programie mógłbym:
        sprawdzać czy dany użytkownik istnieje w bazie
        sprawdzać czy loguje się z innego IP niż zazwyczaj
        sprawdzać czy nie został zbanowany
        sprawdzać czy pewna osoba nie chce zarejestrować się na podobny nick do zbanowanego

    w każdych z tych sytuacji musiałbym pisać kilka poleceń:
        połącz z bazą danych
        załaduj tabelę użytkownicy
            (teraz instrukcje specyficzne dla przypadku)
        zapisz zmiany
        zakończ połączenie
    te 4 rzeczy mogłyby wykonywać się automatycznie, za kulisami, oraz ZAWSZE, przy użyciu CM
    (jako człowiek mógłbym np. zapomnieć dołączyć instrukcję zamknięcia połączenia, w wyniku czego po pewnym czasie serwer
    byłby przeciążony przez niezamknięte połączenia z bazą, CM automatyzuje to i nie muszę się martwić)
    '''
    with open('new_file2.txt', 'x') as file:
        file.write('tu jest tekst')
        file.write(str(a))

    with open('new_file2.txt', 'r') as file:
        caly_tekst_z_pliku = file.read()
        print(caly_tekst_z_pliku)

    with open('new_file2.txt', 'r') as file:
        caly_tekst_z_pliku = file.read()
        print(caly_tekst_z_pliku)

    with open('new_file2.txt', 'w') as file:
        file.write('file overwritten!')

    with open('new_file2.txt', 'r') as file:
        caly_tekst_z_pliku = file.read()
        print(caly_tekst_z_pliku)

    '''
    open ma kilka możliwych trybów działania:
        po przecinku, jako kolejny argument:
            "x" - otwórz do zapisu, tworzy automatycznie plik (ZAKŁADA że go nie ma, jak znajdzie wywala błąd)
            "w" - otwórz do zapisu, nadpisuje wszystko co jest w już istniejącym pliku nową treścią 
            "a" (od 'append') - otwórz do zapisu, zapisuje na koniec pliku w nowym wierszu zostawiając to co już jest
            "r" (od read) - otwórz do odczytu
            otatnie 2 wywalają błąd gdy nie znajdą pliku

    stosując naszą wiedzę z poprzedniego przykładu, napiszmy to w klauzuli try/except 
    '''

    try:
        with open('new_file2.txt', 'x') as file:
            file.write('tu jest tekst')
            file.write(str(a))
    except FileExistsError:
        with open('new_file2.txt', 'a') as file:
            file.write('tu jest tekst')
            file.write(str(a))

    '''
    no dobrze mówiliśmy tu o podstawowych typach zmiennych, tak żeby móc się jakkolwiek wypowiedzieć

    a co gdy mamy wiele takich zmiennych, np. 100 czy 200 czy 1000000? Będziemy je tak wypisywać w nieskończoność?
    Z pomocą przyjść mogą nam listy i słowniki
    '''

    a = []  # deklaracja utworzenia listy
    b = {}  # deklracja utworzenia słownika

    '''
    jak z nich korzystać? jest to niezwykle proste, lecz odmienne dla obu tych typów

    najpierw listy
    '''

    c = [0, 1, 2, 3, 4, 5, 6, 8, 9, True, 12415, 124.26236, 'awphphfaw', 12 + 45]

    '''
    każdy obiekt który chcemy wpisać do tablicy, musi zostać umieszczony w niej po kolei, każdy następny po przecinku
    w ten sposób wypełniamy listę w sposób zwyczajny

    na liście mogą się znaleźć różne typy danych, a nawet skomplikowane obiekty o których będzie więcej później

    a jak w sposób zautomatyzowany wpisać liczby w tablicę, np. generowane przez jakąś funkcję kolegi?

    można skorzystać tutaj z pętli for
    '''
    # a = []  # będziemy wypełniać pustą tablicę, by np. przekazać ją do innego miejsca w programie
    print(a)
    for i in range(20):
        a.append('jestem bogiem pythona')  # każde wykonanie pętli doda do tablicy "a" tekst "jestem bogiem pythona"

    print(a)
    print(c)



