"""
Rozszerzenie obiektowości

Czym jest dziedziczenie oraz co to są metody magiczne
"""

from typing import Union


class Vegetable:
    """
    tak jak w poprzednim przypadku, zdefiniujmy sobie jakąś klasę

    będzie miała ona wszysteki te metody które miały klasy do tej pory, czyli konstruktor, jakieś @property, jakiś inne
    metody magiczne, jak __str__ albo coś w tym stylu

    no dobra, ale co jeżeli chcemy nadać kilku klasom to samo zachowanie? A jeżeli tylko lekko to zachowanie różniłoby
    się od już istniejącego? Nie ma sensu przepisywać 2 razy to samo, zwłaszcza gdy ten element jest w wielu klasach
    potrzebny

    z pomocą przychodzi dziedziczenie, jest to sposób przekazywania grupy zachowań innej klasie, która będzie chciała
    czerpać z tego co już zrobiliśmy

    Zazwyczaj jest tak że dana klasa - mówimy - rozszerza inną klasę; takie podejście jest eksponowane w składni języka
    Java. W pythonie poprzez umieszczenie nazw klas w nawiasie, sugerujemy, że są one rodzicami klasy którą obecnie
    projektujemy

    Często dziedziczenie jest to pewne logiczne rozwinięcie tego co już do tej pory napisaliśmy, albo rozwinięcie
    koncepcji znanej z rzeczywistości

    Tutaj np. deklarujemy klasę `Warzywo`, deklarujemy ją w ten sam sposób co ostatnio, pominiemy więc dokumentację

    TIP: nie powinniśmy tego robić, ze względu na DRY - zasadę `Don't repeat yourself`, ale ze względu na charakter
    materiału (szkoleniowy) pominiemy to na tą chwilę by pokazać pewne różnice w stylu między dwoma klasami w tym
    samym pliku
    """
    def __init__(self, color, mass):
        """
        by wiedzieć więcej jak działa ta klasa zerknij do modułu OOP_podstawy
        """
        self._color = color
        self._mass = mass

    def __str__(self):
        return f'this vegetable weights {self.mass} and has {self.color} color'

    def __repr__(self):
        return f"""{self.__class__.__name__} object
                        id: {id(self)}
                        text: {str(self)}"""

    @property
    def color(self):
        print("inside property")
        return self._color

    @color.setter
    def color(self, value: str):
        print(value, type(value))
        print(f'inside color setter')
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError('value has to be string!')

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value: Union[int, float]):
        print(f'inside mass setter')
        if isinstance(value, (int, float)):
            self._mass = value
        else:
            raise TypeError('value has to be float or int!')


class Plant:
    """
    to co zrobiliśmy powyżej możemy zrobić inaczej, zastanówmy się nad jedną rzeczą

    Czym jest warzywo?

    Najprostszą odpowiedzią może być że jest to poprostu coś do spożywania, ale nie o to chodzi w tym pytaniu

    Chodzi tu o to `do jakiej klasy obiektów należy warzywo`, czyli, czy jest jakaś klasa obiektów do której należy warzywo

    I w sumie jest taka klasa, Warzywo moglibyśmy zaklasyfikować jako obiekt typu `Roślina`
    """
    def __init__(self, color: str):
        self._color = color

    def __str__(self):
        """
        tutaj mała zmiana - jesteśmy w obiekcie `Plant` a nie w warzywie więc trzeba zmienić treść na odpowiednią
        :return: opis rośliny
        """
        return f'this plant is {self._color}'

    def __repr__(self):
        return f"""{self.__class__.__name__} object
                        id: {id(self)}
                        text: {str(self)}"""

    @property
    def color(self):
        print("inside plant property")
        return self._color

    @color.setter
    def color(self, value: str):
        print(value, type(value))
        print(f'inside plant color setter')
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError('value has to be string!')


class Vegetable2(Plant):
    """
    teraz możemy zacząć dziedziczyć po Roślinie, umieszczamy ``Plant`` w nawiasie następującym po definicji klasy

    teraz jesteśmy w stanie odwołać się do wnętrza warzywa używając podobnych wywołań jak w przypadku Rośliny, np.
    deklarując jego kolor, nie musimy już deklarować zmiennej ``color`` ponowanie w konstruktorze, trzeba jednak użyć
    specjalnej funkcji, która jest wbudowana, żeby faktycznie ustawić tą wartość; funkcja ta nazywa się ``super()``

    funkcja super wyszuka w rodzicach klasy ``Vegetable2`` tego co tylko chcemy o ile tam jest:
        zmienna która została zadeklarowana wcześniej w klasie nadrzędnej? Spoko

        funkcja zdeklarowana w klasie nadrzędnej? żaden problem

    Innymi słowy, wszystko co wcześniej zostało zrobione, może być wykorzystane do zrobienia czegoś dodatkowego,
    unokalnego dla rozwiązania postawionego problemu

    skorzystajmy więc z klasy ``Plant`` by użyć już stworzonych w niej rozwiązń, by uprościć sobie pracę
    """

    def __init__(self, color: str, mass: Union[int, float]):
        """
        żadnych tajemnic tu nie ma jeżeli chodzi o masę, przekazujemy ją do obiektu tak jak poprzednio

        nowa rzecz pojawia się natomiast przy deklaracji koloru; korzystamy bowiem z konstruktora klasy nadrzędnej,
        którą w tym wypadk będzie klasa ``Plant``

        przekazujemy ją do konstruktora wywołując funkcję ``super()`` która znajdzie rodzica klasy w której obecnie się
        znajdujemy, a po nim nazwę metody obiektu - tutaj poprostu nasze __init__

        :param color: kolor warzywa
        :param mass: masa warzywa
        """
        self._mass = mass
        super().__init__(color)

    def __str__(self):
        """
        nie jesteśmy już w roślinie, jesteśmy w warzywie, dlatego modyfikując metodę __str__ mamy na względzie to, by
        zachowała się odpowiednio dla warzywa, a nie dla rośliny

        mówimy więc o `nadpisaniu` (`overriding`'u) metody z klasy nadrzędnej, tak by przesłoniła tą która już jest
        w roślinie

        dlatego też nie korzystamy tutaj z funkcji ``super()``

        :return: reprezentacja tekstowa obiektu
        """
        return f'this vegetable weights {self.mass} and is {self.color}'

    def __bases__(self):
        """
        jeżeli jakaś klasa dziedziczy po innej klasie, będzie to widoczne we właściwościach danej klasy

        w każdej klasie powstaje tupla z nazwą klasy po której ona dziedziczy, tupla ta jest nazwana __bases__

        możemy ją zobaczyć, jeżeli zadeklarujemy metodę __bases__ i określimy, że przy jej wywołaniu chcemy zobaczyć po
        jakich klasach bazowych dziedziczy nasza klasa

        robimy to odwołując się do innej właściwości opisującej obiekt - do pola __class__; jest ono elementem każdej
        klasy którą stworzyliśmy albo która jest już stworzona/wbudowana, Pole __class__ zawiera w sobie więcej
        informacji, ale nie będziemy z nich korzystać.

        __bases__ jest też jedną z metod, którą niektórzy programiści nazywają `metodami magicznymi`

        jest ich całkiem sporo, i wszystkie wywodzą się od wspólniej klasy wszystkich klas - klasy ``object``,
        metody te można poznać po charakterystycznym ``__`` przed i po nazwie metody (dlatego też po angielsku
        niektórzy mówią na nie `d-under methods (double under)`; jeszcze inni mówią na nie metody modelu danych, ze
        względu na to, że pozwalają w pewien określony sposób operować na obiektach, albo protokoły

        :return: tupla klas bazowych klasy Vegetable2
        """
        return self.__class__.__bases__

    @property
    def mass(self):
        """
        tak jak i poprzednio definiujemy masę jako @property
        :return: masa warzywa
        """
        print('inside mass getter')
        return self._mass

    @mass.setter
    def mass(self, value: Union[int, float]):
        print(f'inside mass setter')
        if isinstance(value, (int, float)):
            self._mass = value
        else:
            raise TypeError('value has to be float or int!')


class Apple(Plant):
    """
    Dzięki temu że zdefiniowaliśmy klasę nadrzędną Plant, oszczędzimy sobie nieco czasu jeżeli chodzi o pisanie kodu z
    kolorem

    tutaj zdefiniujemy sobie jabłko, jako posiadające z góry określoną masę i kolor

    oczywistym jest więc deklarowanie wielu klas dziedziczących po tej samej klasie
    """
    def __init__(self):
        self._mass = 59.5
        super(Apple, self).__init__(color='red')

    def __str__(self):
        return f'this apple weights {self.mass} and is red'

    @property
    def mass(self):
        """
        i znowu definiujemy masę w podobny sposób

        można byłoby być sprytnym i masę również wrzucić jako komponent rośliny, ale jest rozwiązanie które jest
        jeszcze sprytniejsze, a o którym powiemy sobie później

        :return: masa jabłka
        """
        print('inside mass getter')
        return self._mass

    @mass.setter
    def mass(self, value: Union[int, float]):
        print(f'inside mass setter')
        if isinstance(value, (int, float)):
            self._mass = value
        else:
            raise TypeError('value has to be float or int!')


from abc import ABC, abstractmethod


class MovingObject(ABC):
    """
    stwórzmy sobie klasę, która będzie miała jedną metodę - `move()`

    jest to klasa której obiekty będą mogły się poruszać, w bliżej nieokreślony sposób
    (np. przód tył, na płaszczyźnie, itp.)

    Chcemy jednak ustrzec się błędów, zostawiając metodę w takim stanie jaki tutaj jest (jedyne co mamy to `pass`),
    musimy w jakiś sposób zablokować tworzenie obiektów tej klasy

    przydatny jest tutaj moduł ``ABC`` - `abstract base class`

    to co możemy, po dzeiedziczeniu po klasie ABC, zrobić to jedyie dziedziczyć dalej po tej klasie, ale obiektów klasy
    ``MovingObject`` bezpośrednio nie możemy powoływać

    klasy abstrakcyjne są wykorzystywane (m. in.) do tworzenia tzw. ``interfejsów``, czyli klas, które mają zalążki
    metod, ale te metody wymagają uprzedniej ``implementacji`` - wypełnienia ich kodem potrzebnym w naszym problemie

    dlaczego wogóle takie podejście jest potrzebne? Po co mamy tworzyć klasy abstrakcyjne, jeżeli możemy od razu tworzyć
    coś, co działa, ma pewien wymiar użytkowy? Czemu nie możemy/chcemy po prostu skorzystać z tzw. Duck-typingu?

    Jest to również cięzkie pytanie do odpowiedzi i często pozostawało to dla mnie niejasne, ale mam nadzieję, że
    poniższe tłumaczenie spróbuje wyjaśnić czemu warto czasem skorzystać z klas abstrakcyjnych

    1. NIE MOŻNA POWOŁAĆ OBIEKTU DANEJ KLASY:
        jest to często ważne, by uniemożliwić korzystanie z czegoś co nie ma do końca wykształconych metod;
        korzystanie z takiej klasy może wywołać błędy, albo niektóre metody mogą być użyte w sposób, jaki nie
        chcielibyśmy widzieć u użytkownika naszej biblioteki

    jest to najsłabszy argument w moim mniemaniu, ale przejdźmy dalej

    2. UMOŻLIWIA TWORZENIE INTERFEJSÓW, ZWIĘKSZAJĄCYCH LOGIKĘ W NASZYM KODZIE, CZYNIĄC GO CZYTELNIEJSZYM:
        bardziej konkretny argument, tworząc taką klasę możemy zastrzec, że jest to tylko pewien logiczny zestaw metod
        służący danemu obiektowi do działania.

    pomyślmy więc o naszym obecnym przykładzie - ``MovingObject``

    będzie to pewnego rodzaju interfejs, który przewiduje, że obiekty dziedziczące po nim, jak podpowiada logika, będą
    w stanie się poruszać; może to być dowolny ruch, dlatego pozostawiamy - mówimy - implementację w kwestji
    użwytkownika naszej klasy

    taki interfejs może mieć np. metodę `move()`, oraz coś co zlicza pokonany dystans, jak np. `count_distance_total()`
    u nas będzie jedynie metoda `move()` dla prostoty

    również nie jest to silny argument, możemy skorzystać z wyżej wspomnianego Duck-typingu, by sprawdzić czy faktycznie
    dana klasa ma metody o które nam chodzi - czyli np. w naszym przypadku czy ma zaimplementowaną metodę `move()`,
    i przez to wcale nie musimy tworzyć jakiejś wymyślnej klasy by jasno zdefiniować że obiekt, np. potrafi chodzić

    do zdefiniowania interfejsu wcale nie potrzebujemy też klasy abstrakcyjnej, wystarczy zwykła klasa i klasa która po
    niej dziedziczy

    3. WYMUSZA SPOSÓB KORZYSTANIA Z KLAS DZIEDZICZĄCYCH, PRZY WŁAŚCIWEJ IMPLEMENTACJI:
        deklaracja klasy dziedziczącej po pewnej klasie abstrakcyjnej wymusza więzy na klasie dziedziczącej związanej z
        konkretnym użytkowaniem pewnej klasy

    4. POZWALA PRZEŁADOWAĆ FUNKCJE ``issubclass()`` ORAZ ``isinsance()`` I ZDEFINIOWAĆ DLA NICH NOWE ZACHOWANIE:
        przeładowując funkcje issubclass() oraz isinstance() możemy dojść do sytuacji w której wystarczy że będziemy
        implementowali właściwe metody w danej klasie a kompilator sam będzie troszczył się o to by rozpoznać,
        czy nasza klasa jest podklasą którą wcześniej została już zdefiniowana

    Z punktu widzenia Pythona jest to już jakaś korzyść. Wymuszenie na użytkowniku danej klasy implementację danych
    metod, upewnia nas że obiekty danej klasy będą właściwie powoływane, a jednocześnie możemy wciąż korzystać z
    dobrodziejstw Duck-typingu.

    Może wydawać się to trudne do przyswojenia, więc zostawię przydatne linki:
        PEP 3119: https://www.python.org/dev/peps/pep-3119/

        o module abc: https://docs.python.org/3/library/abc.html#module-abc

        dlaczego warto kozystać z ABC: https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python/3571946

        Duck-typing - definicja: https://pl.wikipedia.org/wiki/Duck_typing

        Podstawa programowania obiektowego - reguła SOLID: https://en.wikipedia.org/wiki/SOLID


    """
    @abstractmethod
    def move(self):
        pass


class BattleUnit(MovingObject):
    """
    Zadeklarujmy sobie jedną z pierwszych klas które dziedziczą po naszym interfejsie ``MovingObject``, niech to będzie
    jednostka bojowa - ``BattleUnit``

    jednostka bojowa, jak to jednostka bojowa, ma też metodę `attack()`, oprócz metody zadeklarowanej w MovingObject

    jest to tak naprawdę już 2-gie dziedziczenie z kolei, wszystkie klasy dziedziczą po klasie ``object``, następnie
    klasa ``ABC`` której użyliśmy to tworzenia MovingObject, dziedziczyła po wbudowanym ``object``, następnie
    stworzyliśmy nasz MovingObject, a teraz BattleUnit który dziedziczy po MovingObject

    a w skróce:
        ``object -> ABC -> MovingObject -> BattleUnit``


    takich dziedziczeń jedno po drugim może być wiele, np.:
        Plant -> Tree -> AppleTree
    """
    def __init__(self):
        """
        Czy obiekt powstanie, nawet jeżeli nie zadeklarujemy właściwego konstruktora? Tak, użyty zostanie domyślny
        konstruktor obiektu, nawet jeżeli nic nie zadeklarujemy tutaj
        """
        pass

    def move(self):
        """
        w tym miejscu wywołujemy metodę move() klasy BattleUnit

        mimo, że wywołujemy `super()` by potem odwołać się do klasy nadrzędnej, to w klasie nadrzędnej metoda ma tylko
        jedną instrukcję - pass, więc jest to raczej zbyteczne

        nie zawsze tak musi być, często w metodzie nadrzędnej np. upewniamy się, że gdy dana metoda jest deklarowana w
        jakiejś klasie, automatycznie dzięki temu stwierdzając, że obiekt po czymś dziedziczy

        nie będziemy daleko szukać, przykład takiej implementacji znajduje się w module collections w podstawowej
        bibliotece Pythona; jak zarzysz do tego modułu spójrz na klasę Container; po deklaracji metod __contains__ którą
        możesz zadeklarować w jakiejkolwiek klasie, Python uzna natychmiastowo, że twoja klasa dziedziczy po klasie
        Container, nawet jeżeli nie zadeklarowałeś jej w nawiasach przy dziedziczeniu - następuje przeładowanie
        isinstance() oraz issubclass()

        takie przeładowanie jest możliwe dzięki __subclasshook__, kolejnej metodzie d-under (sporo ich, ale jest to
        zbyt zaawansowane zastosowanie żeby się tym jak narazie przejmować, później omówimy prostsze : ) )

        link (2-ga odpowiedź): https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python/3571946

        :return: None
        """
        print('changed position!')
        super().move()

    def attack(self):
        print('dealt damage!')


class Vehicle(MovingObject):
    """
    Kolejna klasa dziedzicząca po klasie abstrakcyjnej ``MovingObject``, ale tutaj jest inna implementacja
    """
    def move(self):
        print('moved fast')


class Tank(BattleUnit, Vehicle):
    """
    No dobrze, ale co jeżeli chcialibyśmy pogodzić wiele interfejsów, np. jednostka która się porusza i strzela?

    Nie ma problemu! Możemy dziedziczyć po wielu klasach jednocześnie, wystarczy wypisać je po przecinku w nawiasie w
    deklaracji

    No dobra, ale jest jeden problem:
        Jak pogodzić interfesy które mają tą samą metodę/metody? Która ma być wykorzystana? czy wogóle jest to w jakiś
        sposób regulowane?

    Nie jest to nowy problem, nawet ma swoją nazwę, problem diamentowy

    Problem diamentowy pojawia się wtedy gdy np. dwie klasy dziedziczące po tej samej klasie (u nas jest to BattleUnit),
    implementują metodę zawartą w tej klasie na różny sposób, a następnie w programie istnieje klasa, która dziedziczy
    po obydwojgu z nich. Następuje pytanie po której klasie powinno się dziedziczyć metodę? czy wogóle powinno? Co się
    dzieje przy wywołaniu funkcji super()?

    Zilustrujmy problem schematem:

          O        klasa definiująca metodę `move()` (u nas MovingObject)
        / |
       /  |
      /   |
     /    |
    O     O       klasy implementujące `move()` (u nas Vehicle oraz BattleUnit)
    |    /
    |   /
    |  /
    | /
    O             klasa dziedzicząca po 2 klasach z metodą `move()` (u nas Tank)

    Wiele języków różnie sobie z tym radziło, niektóre uniemożliwiały dziedziczenie po wielu klasach, by nie być na ten
    problem wrażliwym (Java 7 i wcześniej, Java 8 -> ma już wielokrotne rozszeżenia), inne pozostawiały decyzję
    programiście, po której klasie chce dziedziczyć daną metodę i którą implementację wybiera (np. C++)

    Python ma na to odmienne spojrzenie, tak zwane MRO - Method Resolution Order

    MRO jest mechanizmem pozwalającym na wybór metod z klas dziedziczących automatycznie, bez naszej ingerencji
    Ścieżka dziedziczenia powstaje poprzez przegląd klas dziedzicznych, od najwyższej aż do klasy ``object``, z
    wyróżnieniem kolejności dziedziczenia w nawiasach włącznie

    Biorąc przykład z naszego czołgu, obie klasy mają zaimplementowaną metodę `move()`, ale dlatego że w deklaracji
    dziedziczenia ``BattleUnit`` występuje jako pierwsze, to jej implementacja metody `move()` będzie wykonana, gdy
    użyjemy funkcji `super()`
    """
    def move(self):
        print('tank is moving!')
        super().move()  # will use a BattleUnit implementation o the move() method here, not Vehicle ones

    def attack(self):
        """
        nie musimy definiować metody `attack()` na nowo, ale znów chcemy mieć inne działanie niż w implementacji z
        ``BattleUnit``
        :return:
        """
        print('dealt tremendous damage!')


class T34(Tank):
    """
    No dobrze, ale co jeżeli chcemu użyć innej definicji, która była już zadeklarowana? Jak odwołać się do tego inaczej
    niż wynika to z MRO?

    musimy się w takim razie odwołać do tego, jak do metody klasowej, przekazując `siebie` jako referencję

    przy innych metodach byłoby to ważne ze względu na to, że np. musielbyśmy mieć dostęp do pól wewnętrznych
    określonego obiektu, na którym przeprowadzamy jakieś działania (np. obliczenia)

    w naszym przypadku, jeżeli chcielibyśmy skorzystać z metody `move()` klasy ``Vehicle`` zamiast tej danej w MRO
    (BattleUnit), wywołujemy nazwę klasy Vehicle, a potem metodę którą jesteśmy zainteresowani (tu `move()`) i
    przekazujemy `"self"` jako argument (jak w zwyczajnej funkcji
    """
    def move(self):
        print(f'{self.__class__} is moving!')
        Vehicle.move(self)  # here we programatically choose what implementation of move() we need from inherited class


from OOP_podstawy import Polynomial


class ComparablePolynomial(Polynomial):
    """
    Ok, teraz coś lżejszego, ale mogącego rzucić nieco światła na to jak niektóre metody magiczne działają w Pythonie

    Wiedząc co nieco o tym, jak Python jest zbudowany, można wysnuć wniosek, że skoro został napisany w C, można również
    - podobnie jak w C - przeładować różne operatory i metody

    o ile przeładowanie metod nie jest w prost oczywiste, przeładowanie operatorów, np. dodawania jest zdecydowanie
    prostsze. Mieliśmy tego przykład w klasie ``Polynomial``, gdzie zadeklarowaliśmy metodę __add__, tak naprawdę
    nadpisując ją z metod klasy ``object``.

    I tak właściwie dla większości operatorów istnieje metoda modelu danych, która umożliwia w łatwy sposób
    zaimplementowanie przeładowania takiego operatora, pełna lista jest dostępna w dokumentacji Pythona

    link: https://docs.python.org/3/reference/datamodel.html#special-method-names

    tutaj postaramy się napisać 3 z nich:
        czy są równe? -> implementyjemy __eq__ (od `equal`)
        czy jeden jest większy od drugiego? -> implementujemy __gt__ (od `greater than`)
        czy jest mniejszy? -> implementujemy __lt__ (od `lower than`)

    widać że nie jest to takie trudne, a czasem bywa nawet intuicyjne

    jest to podstawa bardziej zaawansowanego podejścia do programowania w Pythonie; jeżeli jest jakaś prosta składnie,
    albo wbudowana funkcja która robi coś z naszym obiektem, prawdopodobnie istnieje metoda __ której implementacja
    umożliwi proste i intuicyjne korzystanie z obieków danej klasy/modelu.

    nadpiszmy sobie metody już obecne w klasie Polynomial, ale napiszmy poprostu odwołanie do metod wbudowanych w tę
    klasę, rozszerzymy dzięki temu funkcjonalność naszego ``Wielomianu`` o możliwości porównania wielomianów ze sobą,
    nie zmieniając podstawowych funkcjonalności
    """
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def __len__(self):
        """
        tutaj używamy super w sposób jaki był używany w starszych wersjach Pythona, nie jest to wymagane, a rezultat
        jest identyczny jak w przypadku użycia zwykłego `super()`
        :return: miara wielkości wielomianu
        """
        return super(ComparablePolynomial, self).__len__()

    def __add__(self, other):
        return super().__add__(other)

    def __eq__(self, other):
        """
        chcemy porównać czy dwa wielomiany są takie same, czyli czy każdy współczynnik przy kolejnych elementach jest
        równy w przypadku obu wielomianów

        :param other: inny wielomian który chcemy porównać
        :return: True jeżeli są takie same, inaczej False
        """
        if len(self) != len(other):
            return False
        checks = [True for x, y in zip(self.coefficients, other.coefficients) if x == y]
        return True if len(checks) == len(self) else False

    def __gt__(self, other):
        """
        jeżeli nasz wielomian jest "większy niż" ten drugi, zwróć True, jak nie to False

        Wielkością wielomianu może być np. wartość ostatniego argumentu, przy wielomianach tej samej długości, lub sama
        długość jeżeli jeden jest ma więcej współczynników od drugiego

        :param other: inny wielomian który chcemy porównać
        :return: True jeżeli jest większy, inaczej False
        """
        if len(self) > len(other):
            return True
        return True if self.coefficients[-1] > other.coefficients[-1] else False

    def __lt__(self, other):
        """
        to samo co w __gt__ ale "mniejszy niż", logika pozostaje ta sama

        :param other: inny wielomian który chcemy porównać
        :return: True jeżeli jest mniejszy, inaczej False
        """
        if len(self) < len(other):
            return True
        return True if self.coefficients[-1] < other.coefficients[-1] else False


if __name__ == '__main__':
    vege1 = Vegetable('blue', 30)
    vege2 = Vegetable2('green', 52.4)
    plant1 = Plant('black')
    print(vege1)
    print(vege2)
    print(plant1)
    print(Vegetable2.__bases__)
    print(vege2.__bases__())
    print(plant1.__class__.__bases__)
    try:
        m_obj = MovingObject()  # Can't instantiate abstract class MovingObject with abstract methods move
    except Exception as e:
        print(e.__class__, e)
    b_u = BattleUnit()
    vh = Vehicle()
    tank = Tank()
    t34 = T34()
    b_u.move()
    vh.move()
    tank.move()
    t34.move()
    tank.attack()
    t34.attack()
    assert isinstance(t34, T34)  # following assertions check wether t34 is object of said type; won't print True if not
    print(True)
    assert isinstance(t34, Tank)
    print(True)
    assert isinstance(t34, MovingObject)
    print(True)

    c_poly1 = ComparablePolynomial(1, 2, 3, 4)
    c_poly2 = ComparablePolynomial(4, 5)
    c_poly3 = ComparablePolynomial(1, 2, 3, 4)
    c_poly4 = ComparablePolynomial(1, 2, 3, 6)

    print(c_poly1 == c_poly3)
    print(c_poly1 > c_poly2)
    print(c_poly1 < c_poly4)
    print(c_poly2 < c_poly3)
    print(c_poly4 > c_poly3)
    print(c_poly1 < c_poly3)
