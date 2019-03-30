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

    to co możemy zrobić to jedyie dziedziczyć to tej klasie, ale obiektów tej klasy bezpośrednio nie możemy powoływać

    klasy abstrakcyjne są wykorzystywane do tworzenia tzw. ``interfejsów``, czyli klas, które mają zalążki metod, ale
    te metody wymagają uprzedniej ``implementacji`` - wypełnienia ich kodem potrzebnym w naszym problemie

    dlaczego wogóle takie podejście jest potrzebne? Po co mamy tworzyć klasy abstrakcyjne, jeżeli możemy od razu tworzyć
    coś, co działa, ma pewien wymiar użytkowy? Czemu nie możemy/chcemy po prostu skorzystać z tzw. Duck-typingu?

    Jest to również cięzkie pytanie do odpowiedzi i często pozostawało to dla mnie niejasne, ale mam nadzieję, że
    poniższe tłumaczenie spróbuje wyjaśnić czemu warto czasem skorzystać z klas abstrakcyjnych

    1. NIE MOŻNA POWOŁAĆ OBIEKTU DANEJ KLASY:
        jest to często ważne, by uniemożliwić korzystanie z czegoś co nie ma do końca wykształconych metod;
        korzystanie z takiej klasy może wywołać błędy, albo niektóre metody mogą być użyte w sposób, jaki nie
        chcielibyśmy widzieć u użytkownika naszej biblioteki

    jest to najsłabszy argument, ale przejdźmy dalej

    2. UMOŻLIWIA TWORZENIE INTERFEJSÓW, ZWIĘKSZAJĄCYCH LOGIKĘ W NASZYM KODZIE, CZYNIĄC GO CZYTELNIEJSZYM:
        bardziej konkretny argument, tworząc taką klasę możemy zastrzec, że jest to tylko pewien logiczny zestaw metod
        służący danemu obiektowi do działania.

    pomyślmy więc o naszym obecnym przykładzie - ``MovingObject``

    będzie to pewnego rodzaju interfejs, który przewiduje, że obiekty dziedziczące po nim, jak podpowiada logika, będą
    w stanie się poruszać; może to być dowolny ruch, dlatego pozostawiamy - mówimy - implementację w kwestji
    użwytkownika

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


class Battleunit(MovingObject):
    def move(self):
        print('changed position!')
        super().move()

    def attack(self):
        print('dealt damage!')


class Vehicle(MovingObject):
    def move(self):
        print('moved fast')


class Tank(Battleunit, Vehicle):
    def move(self):
        print('tank is moving!')
        super(Vehicle).move()

    def attack(self):
        print('dealt tremendous damage!')


class T34(Tank):
    def move(self):
        print(f'{self.__class__} is moving!')


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
