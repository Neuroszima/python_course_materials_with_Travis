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
        while self.current_val <= self.max_point:
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

    metoda ta umożliwia poruszanie się iteratorowi do tyłu
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
        while self.current_val >= self.min_point:
            current_val = self.current_val
            self.current_val -= 1
            return current_val
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

    :param list: lista do przerobienia na iterator
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
    yield 1


# opis do dodania
def multiple_yield_generator():
    yield 1
    yield 2
    yield 'end of file...'


def infinite_yield_generator():
    n = 1
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    print(isinstance(list, typing.Iterator))  # True!

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
    print(isinstance(reversible_iter, typing.Iterator))  # False!

    for i in reversible_iter:
        print("reversible", i, " ", reversible_iter)

    print(reversible_iter)
    reversible_iter = reversed(reversible_iter)
    print(reversible_iter)
    print(next(reversible_iter))

    for i in reversible_iter:
        print('reversed reversible', i)
