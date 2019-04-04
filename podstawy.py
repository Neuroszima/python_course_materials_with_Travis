"""
Pierwszy program

"""

if __name__ == '__main__':
    print("hello world")

    '''
    można używać polskich znaków
    
    '''
    print("coś innego")

    '''
    inny typ umieszczania łańcuchu znaków w funkcji: pojedyńcze apostrofy zamiast cudzysłowu
    można dzięki temu wykorzystać cudzysłów przy wyświetlaniu a apostrof sygnalizując żeby tekst był wyświetlony jako 
    string
    '''
    print('coś innego')
    print('"coś innego"')

    '''
    problematyczne znaki można też przerobić na tzw. znak ucieczki - umieścić przed nim \ by został odczytany dosłownie
    '''
    print("\"hello world\"")

    '''
    możemy też przekazać do print() proste działanie matematyczne, a on zwróci nam wynik
    '''
    print(2 + 2)

    print(2.5)

    from math import pi

    print(pi)

    '''
    możemy definiować stałe w programie
    '''

    a = 0

    b = 3

    '''
    wypisywanie wartości zmiennych w programie
    '''
    print(a)

    print(b)

    '''
    możemy też je sumować
    '''
    print(a + b)

    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = b ** a
    # g = b / a

    print("c = ", c)
    print("d = ", d)
    print("e = ", e)
    print("f = ", f)
    print("g = ", g)
    # print("inf? : ", g)

    '''
    to nie jest tak że wszystkie typy można dodawać do siebie:
    
    np. bezpośrednio nie jesteśmy w stanie dodać tekstu do liczby 
    '''

    # c = 3 + "zosia"

    print(c)

    '''
    musimy skonwertować liczbę na tekst przy użyciu "str()"
    '''

    c = str(3) + "zosia"
    print(c)

    '''
    często chcemy sterować tym, jak program się wykonuje
    
    Chcemy:
    
    powtórzyć pewne operacje na obiekcie X razy
    
    Zadecydować w określonych przypadkach, np. `wystąpiło X, zrób Y, a nie Z`
    
    takie rzeczy możemy zawrzeć w klauzulach sterujących
    
        if warunek:
            instrukcje...
        else:
            inne instrukcje...  
        
        
        FOR element in collection:
            instrukcje...
    '''
    c = 4

    if c < 5:
        print("za malo")
    else:
        print("jest ok")

    c = 7

    if c < 5:
        print("za malo")
    else:
        print("jest ok")

    '''
    powtarzamy instrukcję X razy
    '''

    loops = 5  # ilość wykonań procedury

    for i in range(loops):
        print("program wykonuje pętlę :")
        print(i, " razy ")

    '''
    możemy połączyć te instrukcje i zawrzeć jedną w drugiej
    
    można równierz przerwać przebieg funkcji słowem kluczowym break
    '''

    loops = 55  # ilość wykonań procedury

    c = 1
    for i in range(loops):
        if c < 5:
            print("za malo")
            c += 1
        else:
            print("jest ok")
            break

