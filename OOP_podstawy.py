"""
Podstawy programowania obiektowego

czym jest klasa, czym jest metoda? Co to jest obiekt i jak ma się on do klasy?

te i inne pytania ma za zadanie odpowiedzieć na to pytanie

"""

class HelloWorldWithNothing:
    """
    do tworzenia klas używamy słowa kluczowego "class"

    ten egzemplarz klasy nic nie robi, poprostu jest i tyle
    """
    pass


c = HelloWorldWithNothing()
print(c)
print(type(c))


class Bicycle:
    """
    1 klasa w pythonie która robi coś więcej

    Możnaby zadać pytanie czym wogóle jest klasa?

    Klasa jest kostrukcją, którą tworzymy by opisać pewną grupę obiektów,

    dobrym przykładem prostej klasy jest rower

    pojęcie klasy pozwala sformułować podstawowe cechy danej rzeczy - mówimy na nie OBIEKTY - oraz to jaką interakcję
    ze światem zewnętrznym one przedstawiają

    Jakie więc cechy ma rower? No cóz jest to jednocześnie trudne i proste do zdefiniowania

    Najprostszy opis roweru możnaby określić jako pewien "byt", "przedmiot", "rzecz", czy w końcu "obiekt", który ma następujące własności:
        posiada dwa obiekty zwane "kołami"

        posiada skomplikowany układ mechaniczny zwany "napędem" na który składają się:
            pedały

            łańcuch

            2 wały obracające się, spięte łańcuchem

            przerzutki do zmiany "biegów", czyli zmiany położenia "przekładni" przez co zmieniamy siłę przenoszoną między elementami

        posiada układ zwany kierowniczym z "kierownicą" w postaci pewnego drążka metalowego

        posiada metalowy rdzeń/rusztowanie, spajające te elementy w szególny sposób, zwany "ramą"

    jak widać jest to już bardziej ukonkretyzowany opis czegoś, a nie poprostu zwykłe słowo "obiekt", i opis ten zgadza
    się z faktycznym opisem roweru

    pytania o to jak wygląda dany obiekt trzeba zadać sobie zawsze, gdyż determinuje to jak ten obiekt wygląda

    Determinując klasę obiektu trzeba pomyśleć też o drugiej grupie rzeczy:
        "Jak ten obiekt zachowuje się w rzeczywistości?"

    O zachowaniu obiektu decydują METODY z nim powiązane - mówimy tu o wzorcu zachowań danego obiektu i jego interakcji
    ze światem zewnętrznym

    Co nam po obiekcie który wygląda jak rower jeżeli nie będzie miał funkcjonalności związanych z przemieszczaniem się?

    Co nam po liściach drzew, które, mimo że są zielone, nie mają zdolności fotosyntezy?

    Tutaj trzeba zadać sobie pytania modelowe i zdefiniować zachowanie danego obiektu.

    Jak zchowuje się rower?

    Można pomyśleć o kilku rzeczach:
        obrót pedałów powoduje obrót kół, a gdy jesteśmy na drodze, powoduje zwiększenie prędkości

        przerzutki mają możliwość regulacji, przestawiając łańcuch i zmieniając rozkład sił w układzie mechanicznym
            powodując zwiększenie prędkości obrotu kół, kosztem wkładanej siły

        obrót kierownicą pozwala nam zmienić kierunek jazdy na płaszczyźnie
    na razie te 3 rzeczy wystarczą :)

    """

    def __init__(self, color, type, gears=5, wheel_width=2, company="Bicycle Industries"):
        """
        Można do tego podejść inaczej, ja lubię na to spojrzeć również z następującej perspektywy:
            Zadaję sobie pytanie:
                "Gdybym miał fabrykę pewnego rodzaju obiektu, o jakich cechach wyglądu musiałbym pomyśleć, aby choć częściowo był podobny do tego, jak wygląda w rzeczywistości?"

        Odpowiadając sobie na to pytanie, mógłbym w pełni stworzyć wybrany obiekt o niemalże identycznym wyglądzie, lub
        po prostu miałbym pewną "linię montażową" do tworzenia podobnej klasy obiektów.

        taką linią montażową jest właśnie metoda "__init__"

        jakie więc dane możemy wysłać do "fabryki w naszym rowerowym przypadku?

        Tutaj, w moim przypadku wysyłam:
            kolor

            typ (np. czy jest to góral, czy kolażówka)

            rodzaj przerzutek (np. ilość biegów)

            szerokość opon

        przerabiając te dane moja fabryka wypluwa mi rower, z którym mogę następnie zrobić co tylko chcę

        w miarę jak nasza "fabryka" zaczyna pracę, może rzucić się w oczy pewna koncepcja - zmienna `"SELF"`

        jest to niezwykle prosta ale i ważna koncepcja w programowaniu obiektowym, mówimy tutaj o "WSKAŹNIKU" na samego
        siebie, w pewnym rodzaju jest to coś, co identyfikuje i gwarantuje niepowtarzalność jednostki pochodzącej z danej
        klasy

        w przypadku rowerów, jest to rodzaj dosłownego powiedzenia "to jest ten obiekt - ja", wymaga to nieco podejścia
        filozoficznego, ale staje się to niezwykle zrozumiałe, jak samemu się tego użyje. Wskaźnika `"SELF"` używa się
        wewnątrz obiektu by odnieść się do konkretnej jego właściwości.

        Odnosząc się do konkretnego przykładu, składnia:
            `self.color`
        w języku ludzkim może zostać przetłumaczona jako:
            `mój.color`

        poniżej znajduje się dokumentacja (to co czytasz z resztą również nią jest) dotycząca danych wejściowych

        słowo kluczowe ":param" i następująca po nim nim nazwa parametru (obia zmknięte w dwukropkach) daje znak
        edytorowi w IDE by odczytał to jako opis parametru wejściowego, a następujące po nim słowa jako krótki
        opis wejścia tego parametru

        :param color: kolor roweru który ustawiamy
        :param type: typ roweru (np. góral)
        :param gears: ilość przerzutek
        :param wheel_width: szerokość opon
        """
        self.company = company
        self.color = color
        self.type = type
        self.gears = gears
        self.wheel_width = wheel_width

    def __str__(self):
        """
        no dobrze ale ja wyświetlić jakiekolwiek informacje o tym rowerze?

        Można to zrobić na różne sposoby, najprościej jest wyraźić opis słowami, tutaj przydaje się napisanie metody
        wewnętrznej w klasie, która taką reprezentację wygeneruje

        taką metodą jest metoda "__str__", gdy w innym miejscu programu zostanie użyta funkcja:
            "str(`tutaj_twój_obiekt`)"

        program będzie w stanie odwołać się do metody __str__ i wygenerować poprawny opis

        inaczej poad to co ma dostępne domyślnie, czyli adres obiektu w pamięci komputera

        :return: reprezentacja tekstowa roweru
        """
        info = f"""To jest rower:
            typ: {self.type}
            kolor: {self.color}
            firma: {self.company}
            liczba przerzutek: {self.gears}
            szerokość opon: {self.wheel_width}
        """
        return info

    def __repr__(self):
        return str(self)


    '''
    no dobrze mamy obiekt, ale jak odczytać to co on przedstawia?
    
    w tym celu wymyślono pewien sposób zapisu; utworzono tak zwane metody pobierające i ustawiające
        (gettery i settery)
        
    w myśl tego, żadna zmienna nie powinna być wczytywana bezpośrednio w programie, ale za pośrednictwem tych metod
    '''

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_gears(self):
        return self.gears

    def get_wheel_type(self):
        return self.wheel_width

    def get_company(self):
        return self.company


class HelloWorld:
    """
    Wypisuje "hello world" przy utworzeniu
    """

    def __init__(self):
        print("Hello world from class")


c = HelloWorld()
d = HelloWorld()

print(type(c), type(d))


class Polynomial(object):
    """
    klasa reprezentująca wielomian

    """
    def __init__(self, *args):
        """
        inicjalizuje obiekt klasy wielomian nieokreślonego rzędu. Jako argumenty przyjmuje serię parametrów jako
        kolejne współczynniki przy członach o rosnącej potędze

        :param args:
        """
        print(args)
        self.coefficients = [arg for arg in args if isinstance(arg, (int, float))]

    def __len__(self):
        """
        odpowiednik "długości" obiektu klasy wielomian

        co może być takim odpowiednikiem? Np. współczynnik przy członie o najwyższej potędze - rząd wielomianu

        :return: długość wielomianu
        """
        return len(self.coefficients)

    def __repr__(self):
        """
        reprezentacja naszego wielomianu

        :return: obiekt "repr()" wielomianu
        """
        return str(self)

    def __str__(self):
        """
        przedstaw TEN obiekt jako łańcuch znaków
        :return: obiekt "str()" wielomianu
        """
        info = [f" + {self.coefficients[i]}x^{i}" for i in range(1, len(self))]
        return f"{self.coefficients[0]}" + ''.join(info)

    def __add__(self, other):
        """
        w metodzie __add__, możemy zdefiniować zchowanie jakie będzie przejawiać działanie `dodawania` dwóch obiektów
        o klasie `Polynomial`

        :param other: inny wielomian
        :return: wielomian zsumowany
        """
        scf = self.coefficients
        ocf = other.coefficients
        new_scf = []
        new_ocf = []
        if len(scf) < len(ocf):
            # new_scf = [scf[i] if scf[i] else 0 for i in range(len(ocf))]
            for i in range(len(ocf)):
                try:
                    new_scf.append(scf[i])
                except IndexError:
                    new_scf.append(0)
            new_ocf = ocf
        else:
            # new_ocf = [ocf[i] if ocf[i] else 0 for i in range(len(scf))]
            for i in range(len(scf)):
                try:
                    new_ocf.append(ocf[i])
                except IndexError:
                    new_ocf.append(0)
            new_scf = scf
        return Polynomial(*[coeff_self + coeff_other for coeff_self, coeff_other in zip(new_scf, new_ocf)])


if __name__ == '__main__':
    bike = Bicycle("blue", "mountain", 6)
    print(bike)
    print(bike.get_color())
    print(bike.color)
    print(bike.get_gears())
    polynom = Polynomial(1, 2, 3, 4, 5)
    polynom2 = Polynomial(3, 5)
    print(polynom)
    print(polynom2)
    poly3 = polynom + polynom2
    print(poly3)
    polynom2 = Polynomial(3, 5)
    polynom = Polynomial(1, 2, 3, 4, 5)
    poly4 = polynom + polynom2
    assert str(poly3) == str(poly4)

