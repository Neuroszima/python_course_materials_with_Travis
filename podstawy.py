"""
Pierwszy program

"""

if __name__ == '__main__':
    print("hello world")

    """
    można używać polskich znaków
    
    """
    print("coś innego")

    """
    każdy program ma wbudowane funkcje, tu np. możemy użyć sum(elementy)
    """

    print(2 + 2)

    print(3.40958028)

    from math import pi

    print(pi)

    """
    możemy definiować stałe w programie
    """

    a = 0

    b = 3

    """
    wypisywanie wartości zmiennych w programie
    """
    print(a)

    print(b)

    """
    możemy też je sumować
    """
    print(a + b)

    c = a + b

    print(c)


    """
    często chcemy sterować tym, jak program się wykonuje
    
    Chcemy:
    
    powtórzyć pewne operacje na obiekcie X razy
    
    Zadecydować w określonych przypadkach, np. `wystąpiło X, zrób Y, a nie Z`
    
    takie rzeczy możemy zawrzeć w klauzulach sterujących
    
            IF
            
            FOR
            
    
    """
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

    """
    powtarzamy instrukcję X razy
    """

    loops = 5  # ilość wykonań procedury

    for i in range(loops):
        print("program wykonuje pętlę :")
        print(i, " razy ")

    """
    możemy połączyć te instrukcje i zawrzeć jedną w drugiej
    
    można równierz przerwać przebieg funkcji słowem kluczowym break
    """

    loops = 55  # ilość wykonań procedury

    c = 1
    for i in range(loops):
        if c < 5:
            print("za malo")
            c += 1
        else:
            print("jest ok")
            break

