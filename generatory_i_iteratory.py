"""
generatory i iteratory, oraz dlaczego warto ich używać
"""
import typing


class MyIter(object):
    """
    ok pora przejść do iteratorów

    czym jest iterator? W skrócie jest to obiekt, o którym możemy powiedzieć, że możemy zwracać jego zawartość bądź
    wykonywać jego treść element po elemencie.

    Może narzucać się, że logicznym jest twierdzić, że lista jest iteratorem, ale tak nie jest. Lista jest tylko zbiorem
    uporządkowanych danych o którym można powiedzieć, że można po nim "iterować"

    Czym jest więc iterator? to jakaś funkcja? może jakaś klasa? a może jakaś implementacja jeszcze czegoś innego?

    Iteratorem w Pythonie jest klasa która implementuje 3 rzeczy:
        metode __init__() - bo coś chcemy mieć w tym iteratorze

        metodę __iter__() - w ten sposób zwracana jest instancja iteratora

        metodę __next__() - w ten sposób jest determinowany kolejny element

    W iteratorze mamy jakiś logiczny początek i koniec, tj. definiujemy skończony zestaw danych/zawartości, albo
    poprostu tworzymy iterator, który działa do pewnego momentu.

    W jaki sposób to zrobić? zaimplementujmy najpierw podstawowe metody a w nich całą potrzebną logikę
    """
    def __init__(self, max_point, current_val=0):
        """
        nie definiujmy tutaj property, do działania nie jest on konieczny

        chcemy jedynie zaprezentować podstawowe działanie iteratora i jego deklarację

        :param stop_point: jakiś argument dla iteratora
        """
        self.min_point, self.current_val = 0, current_val
        self.max_point = max_point

    def __iter__(self):
        """
        tutaj definiujemy co ma zostać zwrócone jako instancja iteratora

        zazwyczaj jest zwracany obiekt `self` - obiekt sam jest iteratorem

        :return: obiekt iteratora
        """
        return self

    def __next__(self):
        """
        Tutaj decydujemy jakie elementy mają być zwracane po kolei i w jaki sposób

        A co jeżeli elementów już nie będzie? np. tablica/tabela z danymi się skończy? Wewnętrznie Python stworzony
        jest w taki sposób, by w takich wypadkach podnoszony był wyjątek ``StopIteration``

        Najprostszym iteratorem jest klasa, która tworzyłaby sekwencję liczb, do podanej liczby włącznie. Nasza metoda
        __next__ wyglądałaby w takim wypadku jak ta poniżej

        Deklarując te metody nie tylko możemy korzystać z pętli for, albo jakiegoś list comprehension, by zwracać
        poszczególne wartości. Iterator "pamięta" swój stan, i możemy wywołać go kiedy chcemy, by zwrócił nam kolejną
        wartość. Robimy to funkcją next().

        :return: następny element
        """
        while self.current_val < self.max_point:
            current = self.current_val
            self.current_val += 1
            return current
        else:
            raise StopIteration('no more values you want to return')


class MyReversedIter(object):
    """
    oprócz metody __iter__ oraz __next__ iteratory mogą deklarować metodę __reversed__

    nasze rozwiązanie jest jednak zbyt scustomizowane, by tego rozwiązania na razie użyć. Stwórzmy na ten czas klasę,
    która będzie iterowała z góry do dołu, z zadeklarowaniem wartości

    metoda __next__ będzie tutaj umożliwiać poruszanie się iteratorowi od wartości najmniejszej do największej
    """
    def __init__(self, max_point, current_val=None):
        self.min_point = 0
        self.max_point = max_point
        if current_val is not None:
            self.current_val = current_val
        else:
            self.current_val = max_point

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_val > self.min_point:
            self.current_val -= 1
            # current_val = self.current_val
            return self.current_val
        else:
            raise StopIteration('no more values you want to return')


class MyReversibleIter(object):
    """
    Teraz zadeklarujmy klasę która będzie chodzić zarówno w przód i w tył

    przydadzą nam się dwie poprzednie klasy które zadeklarowaliśmy wcześniej. Będziemy trzymać instancję jednej z nich
    i odwoływać się do metody next tego iteratora gdy będziemy tego potrzebować. Następnie __reversed__ podmieni nasz
    obecny iterator na taki, który będzie iterował, ale w odwrotnej kolejności, następnie zwracając siebie z nowym
    iteratorem

    Dzięki temu będziemy mieli prostą otoczkę do tego, by zawracać kiedy chcemy. Nie można zwrócić tej samej instancji
    naszej klasy w taki sposób by sama została zmieniona kolejność. Wyjątek StopIteration uniemożliwia zawrócenie
    iteracji
    """
    def __init__(self, end_point, current_value=0):
        self.iterator = MyIter(end_point, current_val=current_value)
        self.forward = True

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def __str__(self):
        info = " min="+str(self.iterator.min_point)+\
               " max="+str(self.iterator.max_point)+\
               " current="+str(self.iterator.current_val)
        return info

    def __reversed__(self):
        if self.forward:
            self.forward = False
            self.iterator = MyReversedIter(self.iterator.max_point, self.iterator.current_val)
            return self
        else:
            self.forward = True
            self.iterator = MyIter(self.iterator.max_point, self.iterator.current_val)
            return self


def iter_iterator(mylist):
    """
    można jednak zadeklarować iterator zdecydowanie prościej, wystarczy skorzystać z typów wbudowanych w Pythonie, jak
    np. z listy, i stworzyć, lub włączyć go w iterator

    Jak to zrobić? można ponownie zadeklarować klasę, tym razem przekazując tą listę jako argument do inicjalizacji
    obiektu, a następnie zdefiniować takie same metody jak wcześniej. Lista jest typem iterowalnym, więc takie metody
    jak __reversed__ można by było łatwiej zaimplementować; spójrz np. na iterator klasowy zadeklarowany w przykładzie
    ze strony: http://zetcode.com/python/reverse/  (tam gdzie jest `class Vowels()`)

    Ale można jeszcze prościej! Można zdefiniować iterator przy pomocy wbudowanego ``iter()``; w ten sposób
    powstanie iteratora z naszej listy jest banalne. Warto zapamiętać jednak fakt, że klasowe iteratory można łatwiej
    dostosować do naszych potrzeb, np. dodając przydatne metody do klasy

    :param mylist: lista do przerobienia na iterator
    :return: iterator z listy
    """
    return iter(mylist)


def itetools_repeat_iterator(element, nr_of_times):
    """
    jeszcze inną metodą jest skorzystanie z modułu ``itertools``, tutaj generujemy iterator jako sekwecję powtarzaną
    tego samego elementu

    :param element: powtarzany element
    :return: iterator z elementu
    """
    import itertools
    return itertools.repeat(element, nr_of_times)


#  opis do dodania
def generator1():
    """
    a gdzie w tym wszystkim są generatory???

    Generator jest to również iterator, można by szczerze powiedzieć, że są nie rozróżnialne, jednak pod spodem jest
    kilka ciekawych rzeczy które możnaby powiedzieć o generatorach

    zazwyczaj mówi się o generatorach, że są to takie "funkcje, które zamiast return mają yield". I jest to prawda,
    projektanci języka stwierdzili, że można za pomocą słowa kluczowego yield, ze zwykłaej funkcji która ma `return`,
    nadać właściwości iteratora takiej funkcji umieszczając w niej yield

    nie jest to jednak do końca iterator, fakt, z punktu widzenia iteratorów można do tego podejść w niemalże identyczny
    sposób, znów definiować klasę, na nowo definiować metodę __next__, zamiast `return` dać `yield` i to jest wszystko,
    a my pod względem zaprojektowania nie widzimy żadnej różnicy

    generator jednak robi coś sprytniejszego - sam definiuje za nas metodę __next__

    czym jest jednak to __next__? jest to (albo raczej, możemy to przybliżyć do) linia kodu po słowie kluczowym yield
    które zostało wykonane. Wraz z linią kodu zostaje zapamiętany również stan obiektu, tak, byśµy mogli do niego
    wrócić przy kolejnym wywołaniu

    spójrzmy na poniższą funkcję, zgodnie z tym co tutaj napisałem, funkcja powinna przy pierwszym wykonaniu zwrócić 1,
    a następnie wywołać wyjątek StopIteration, jak w iteratorze, bo 1 już zwróciliśmy, a dalej nic już nie ma

    aby skorzystać z generatorowej funkcji, nie będziemy jej wywoływać od razu z (), najpierw przypiszmy ją do zmiennej,
    by nie stracić bazowego stanu generatora który został utworzony przy uruchomieniu programu z tego modułu

    :return: 1, dalej podnosi StopIteration
    """
    yield 1


# opis do dodania
def multiple_yield_generator():
    """
    przez to że generatory przechowują swój stan w pamięci, możemy napisać kilka yield w jednej funkcji

    generator zatrzyma swoje działanie na kolejnym, by wczytać go przy następnym wywołaniu funkcji next()

    :return: wartośc w zależności od ilości next()
    """
    yield 1
    yield 2
    yield 'end of file...'


def infinite_yield_generator():
    """
    dzięki temu że funkcja "pamięta" gdzie skończyła, możemy zdefiniować sobie generatory, które mają nieskończone
    pętle

    dalczego generatory warto stosować?

    cóż jedna rzecz jest szczególnie ważna a jest nią to że:
        generatory pamiętają swój stan, listy zajmują dużo pamięci

    jest to najważniejsza zaleta generatorów, poniżej mamy sekwencję liczb od jednego do nieskończoności! chyba nie
    masz takiej dobrej pamięci żeby wszystkie liczby pomieścić, nie?

    stosując generator możemy znacznie zredukować jej zużycie na gorszych maszynach, poza tym generatory dziedziczą po
    iteratorach jeszcze jedną rzecz - są leniwe

    yield zwraca wartość jednocześnie zapamiętując swój stan. Możemy w między czasie wykonać całe mnóstwo rzeczy po
    zwróceniu wartości, a nie musimy zrzucać wszystkiego jednocześnie do listy, jak byśmy to zrobili tradycyjnie. Takie
    podejście umożliwia lepsze wykorzystanie czasu procesora, gdyż gdy czekamy na wynik innego polecenia, zazwyczaj
    tradycyjnie nie jest możliwe zatrzymanie programu od tak. Z generatorem zapisując stan możemy przenieść moc gdzie
    indziej, czekając na dane z innych miejsc, np. z internetu. Trzymając w pamięci staj 1 obiektu, nie trzymamy też
    100000000 rekordów historii naszego programu.

    Dlatego że generator umożliwia podejście z lepszym wykorzystaniem zajętości procesora jest często mylony z szybszym
    wykonaniem danego wątku, co nie jest prawdą. Obliczenie zawsze musi się odbyć. Wczytywany jest co prawda stan
    generatora, a gdy stan ten leży w pamięci o niskim czasie dostępu (np. L1) faktycznie moglibyśmy zwrócić uwagę na
    poprawę czasu wykonania, w stosunku do 10000000 wartości w listach. Nie zawsze jednak jest to prawda.

    :return: tyle n ile mania woli
    """
    n = 1
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    print(isinstance(list, typing.Iterator))  # False!

    new_iter = MyIter(10)
    print(isinstance(new_iter, typing.Iterator))  # True!
    for i in new_iter:
        print(i)

    try:
        next(new_iter)
    except StopIteration as si:
        print(si)
        print('nothing more')

    new_iter2 = MyReversedIter(10)
    print(isinstance(new_iter2, typing.Iterator))  # True!
    for i in new_iter2:
        print('reversed', i)

    try:
        next(new_iter2)
    except StopIteration as si:
        print(si)
        print('nothing more')

    reversible_iter = MyReversibleIter(10)
    print(isinstance(reversible_iter, typing.Iterator))  # True!

    for i in reversible_iter:
        print("reversible", i, " ", reversible_iter)

    print(reversible_iter)
    reversible_iter = reversed(reversible_iter)
    print(reversible_iter)
    print(next(reversible_iter))

    for i in reversible_iter:
        print('reversed reversible', i)

    new_gen = generator1  # here we copy a function that returns generators
    print("")
    print(new_gen)
    print(new_gen())
    # all those below will return "1" since they call a function saved in new_gen for new instance of the
    # generator each time, and then invoke next() on themselves
    print(next(new_gen()))
    print(next(new_gen()))
    print(next(new_gen()))
    print("")
    gen = new_gen()  # here we save an actual generator to memory
    print(next(gen))  # should return "1"
    # print(next(gen))  # now this raises "StopIteration"
    multi_gen = multiple_yield_generator()
    print("")
    print(next(multi_gen))  # 1
    print(next(multi_gen))  # 2
    print(next(multi_gen))  # 'eof'
    infi_gen = infinite_yield_generator()
    for i in range(10):  # will print 1 to 10, we don't want an infinite loops
        print(next(infi_gen))

    # and did it save state?
    print(next(infi_gen))
