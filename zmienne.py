

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
    pygod = 'jestem bogiem pythona'
    print(a)
    for i in range(20):
        a.append(pygod)  # każde wykonanie pętli doda do tablicy "a" tekst "jestem bogiem pythona"

    print(a)
    print(c)

    '''
    mamy listę z elementami, ale czy możemy się odwołać do konkretnego jej elementu? 
    
    No pewnie że tak, odwołujemy się do niego podając numer w kolejności w jakiej element ten występuje
    w tablicy/liście, zaczynając od zera:
    '''

    print(c[0])
    print(c[5])
    print(c[10])
    # print(c[22])  # wywali błąd

    '''
    podmiana elementów również jest możliwa, również wystarczy odnieść się do elementu o pożadanym numerze, i przyrównać
    do niego nową wartość
    '''

    print(c[0])
    c[0] = pygod
    print(c[0])

    a = '''
    tekst tej pomocy zostanie przyrównany do zmiennej, jednocześnie wykonując "split"
    
    jest to specjalny rodzaj tworzenia tablicy z tekstu, gdzie elementami tablicy będą wyrażenia które będą rozdzielone
    po kluczu
    
    np. żeby otrymać listę wyrazów z tekstu który czytasz, użyjemy jako klucza znaku " " (spacji)
    '''.split(" ")
    print(a)

    '''
    Jak widać tekst został rozdzielony po spacjach i otrzymaliśmy listę, a jak ją z powrotem złączyć?
    
    Wykorzystamy wbudowaną w string funkcję "join", działa na takiej samej zasadzie jak split, ale odwraca jego proces
    
    Widzimy, też pewną prawidłowość; stosujemy "split" a także będziemy stosować "join" na już zadeklarowanym łańcuchu 
    znaków; nie musimy się martwić o to, by przyrównać go do zmiennej, już sam tekst nią jest
    '''

    print(" ".join(a))

    '''
    do tworzenia list możemy użyć jeszcze jednej przydatnej formuły, jaką jest `list comprehension`
    
    list comprehension pozwala na skompresowanie tworzenia listy pętlą for, umieszczając ją w deklaracji jej utworzenia
    (pomiędzy nawiasami kwadratowymi)
    
    nie potrzebujemy więc używać a.append(`argument`), wystarczy użyć list comprehension
    '''

    l = [' coś ' for i in range(20)]
    print(l)

    '''
    w pętli for możemy użyć więcej niż jednej kolekcji do iterowania po danych; używamy funkcji 
    zip(element1, element2...), która pozwala nam zadeklarować te zmienne jako 2 listy po których mamy iterować
    
    pamiętajmy że muszą to być listy o tej samej długości!
    '''

    poly3 = []

    polynomial1 = [1, 3, 7, 9]
    polynomial2 = [3, 4, 7, 0]

    for coeff1, coeff2 in zip(polynomial1, polynomial2):
        poly3.append(coeff1 + coeff2)

    '''
    a w list comprehension
    '''

    poly4 = [coeff1 + coeff2 for coeff1, coeff2 in zip(polynomial2, polynomial1)]

    print("poly3 = ", poly3)
    print("poly4 = ", poly4)

    '''
    mamy również możliwość tworenia czegoś co przypominałoby wielowymiarowe tablice; jak to zrobić?
    
    cóż jest to po prostu tablica zawarta w tablicy
    '''

    matrix = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 1, 1]
    ]
    matrix2 = [
        [1, 0, 2],
        [1, 1, 0],
        [1, 0, 6]
    ]

    '''
    dostaliśmy 2 macierze 3x3 z odpowiednio wstawionymi parametrami
    
    mnożenie macierzy przy użyciu gwiazdki powoduje mnożenie "element po elemencie"
    
    mnożenie przy użyciu "@" oznacza właściwe mnożenie macierzowe, znane z akademickiego kursu matematyki
    '''
    import numpy as np

    matrix2 = np.array(matrix2)
    matrix = np.array(matrix)

    matrix3 = matrix * matrix2
    matrix4 = matrix @ matrix2
    matrix5 = matrix2 @ matrix

    print(matrix3, "\n\n", matrix4, "\n\n", matrix5)

    '''
    powiedzmy sobie teraz o słownikach, słowniki również zapisują wiele danych w sobie, tak samo jak lista
    
    odmiennie od list zapis w słownikach realizuje się jako zapis w stylu klucz=wartość
    '''

    # b = {}  # deklaracja słownika

    b['klucz'] = 'wartość'
    b['s2'] = 2

    '''
    jak widać kluczem jest zawsze string, wartością może być wszystko, łącznie z innym słownikiem
    
    odwołanie się do wartości przebiega analogicznie
    '''
    print(b['klucz'])
    print('s2 : ', b['s2'])

    print(b)
    '''
    jeżeli chcielibyśmy zainicjować słownik z jakimiś wartościami na starcie, wpisujemy je również jako pary
    klucz wartość, ale w określony sposób; definiuje się je jako:
        `"key" : value`
    
    a więc wartości następują po dwukropku
    '''
    value = 3.14

    d = {'a' : 3,
         'another dict' : {
             'key': value
         },
         'something': 'else'}

    '''
    w pętli for możemy odwołać się zarówno do kluczy jak i wartości
    '''

    for key, value in d:
        print(key, ' ',  value)

    '''
    warto zaznaczyć że słowniki są wykorzystywane we frameworku Django; przekazuje się w nich tzw. kontekst, który
    będzie następnie wyświetlany na stronie
    '''
