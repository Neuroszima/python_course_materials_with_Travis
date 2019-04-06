"""
moduł - dekoratory

"""
from time import sleep, time
from datetime import datetime


def fetch_data(server_address='www.server.com/api', data_type='int32'):
    """
    najprostszym i najbardziej popularnym przykładem do omawiania dekoratorów jest funkcjonalność mierzenia czasu
    wykonania danej procedury czy też funkcji. Wyobraźmy sobie, że mamy już pewną procedurę, np. pobieramy dane z bazy
    i coś z nimi robimy. Funkcja taka zazwyczaj czeka na odbiór danych i sprawdza je, czy na pewno są odebrane we
    właściwej formie.

    Załóżmy że coś w naszym programie nie gra i chcemy sprawdzić gdzie dokładnie, sprawdzając, jak długo dana
    funkcja/metoda/procedura się wykonuje

    Poniżej znajduje się funkcja pobierająca dane z serwera, pobiera je i przetwarza do odpowiedniego formatu podanego
    w jej argumentach

    chwilę to trwa

    :param server_address: address of a server which will be called to fetch data from
    :param data_type: type of data, default int32
    :return: data in desired format
    """
    print('fetching data...')
    sleep(0.5)  # simulating the time taken to fetch data from server
    print('preprocessing data...')
    sleep(0.5)
    print('done!')
    data = ['data']
    return data


def add(a, b=1):
    return a + b


def subs(a, b):
    return a-b


def fetch_data_timed(server_adderss='www.server.com/api', data_type='int32'):
    """
    Zastanówmy się nad rozwiązaniem z umieszczaniem pomiaru czasu przed i po wykonaniu funkcji w głównym kodzie naszej
    aplikacji

    musimy napisać/skopiować to zachowanie w wielu miejscach, a następnie nie zapomnieć usunąć tej części kodu ze
    wszystkich części naszej biblioteki po naszej "diagnozie", co jest uciążliwe i można łatwo zapomnieć coś usunąć

    czy jest prostsze rozwiązanie? Oczywiście. możemy np. zawrzeć to zachowanie w funkcji bezpośrednio.

    :param server_adderss:addres of a server which will be called to fetch data from
    :param data_type: type of data, default int32
    :return: data in desired format
    """

    print('fetching data...')
    start = time()
    sleep(0.5)
    print('preprocessing data...')
    sleep(0.5)
    print('done!')
    data = ['data']
    end = time()
    time_taken = end - start
    print(time_taken)

    return data


def add_timed(a, b=1):
    start = time()
    result = a + b
    end = time()
    time_taken = end - start
    print(time_taken)
    return result


def subs_timed(a, b):
    start = time()
    result = a + b
    end = time()
    time_taken = end - start
    print(time_taken)
    return result


def print_helloworld():
    """
    nieźle! nasz właściwy kod poniżej, w bloku "__main__" jest czystszy i bardziej czytelny, gdyż schowaliśmy pożądane
    zachowanie w naszych funkcjach

    ale czy da się jeszcze lepiej? Co jeżeli mamy 100 różnych funkcji na przestrzeni całego programu? Np. takich
    krótkich, jak ta tutaj, gdzie wpisanie w nią logiki zajęłoby więcej linii niż sama funkcja?
    """
    print('\n', 'in hello world')
    print('hello world')


def print_function_name(function):
    """
    Z pomocą przychodzą właśnie dekoratory

    czym są dekoratory?

    jest to dość specyficzne rozwiązanie pewnego nierzadko spotykanego problemu, ogólnie rzecz ujmując jest to
    sposób ubierania funkcji w pewne zachowania, które chcemy zastosować w specyficznych miejscach

    w naszym przykładzie chcemy ubrać nasze 3 funkcje w możliwość zmierzenia czasu ich wykonania, zróbmy to za
    pomocą dekoratora

    W ramach wstępu musimy powiedzieć o jednej rzeczy - python jest żywym językiem, wszystko jest kodem który się
    wykonuje nawet deklaracja definicji funkcji czy też utworzenia definicji klasy (użycie gdziekolwiek ``class``)

    Dzięki temu wszystko co do tej pory widzieliśmy możemy potraktować jako zmienną, nie ważne czy jest to np.
    klasa czy funkcja. Możemy przypożądkować ją do zmiennej i na niej operować jakby była zwykłą zmienną

    co to oznacza? podstawową wiedzę już mamy, możemy przekazać zmienną do funkcji. A co jeśli tą zmienną bęzie inna
    funkcja? Jest to podstawą dekorowania funkcji w inne zachowania

    Rozpatrzmy prostszy przypadek, chcemy wypisać w konsoli nazwę funkcji, która jest do niej podawana. Przekazujemy
    więc funkcję do funkcji jako jej argument, a następnie wyświetlamy `function.__name__` w ``print()``. Możemy nawet
    spróbować wywołać funkcję i zobaczyć co ona zwraca. Tutaj przekażemy sobie poprosy hello_world, nie przyjmującą
    żadnych argumentów, gdyż troszkę skomplikowałoby to naszą składnie

    zamiast tylko wyświetlać jej nazwę, możemy też zwrócić wynik oryginalnej funkcji

    nie jest to prawdziwy dekorator, lecz wstęp do ich omawiania, ale rezultat końcowy będzie podobny
    """
    print('in "print function name": ')
    result = function()
    print(function.__name__)
    return result


def print_name(function):
    """
    w funkcji powyżej ubraliśmy funkcję w zachowanie innej funkcji; wypisaliśmy je nazwę, a następnie wewnątrz
    funkcji ubierającej, wykonaliśmy funkcję ubieraną, zwracając na końcu jej rezultat, by odzyskać jej pierwotny
    wynik

    a jak zrobilibyśmy to w dekoratorze? W poprzednim przypadku nie mieliśmy za bardzo możliwości przechwycenia
    wartości funkcji, które zostałyby do niej przekazane.

    Narazie się tym nie przejmujmy, napiszmy jednak prawdziwy dekorator. Nie będzie miał obsługi danych wejściowych,
    lecz będzie działał tak, jak każdy dekorator który normalnie piszemy w Pythonie

    Warto zwrócić uwagę, że piszemy definicję nowej funkcji, w funkcji. Mówimy o tej funkcji, że jest to tak zwany
    "wrapper" czyj funkcja zawierająca pewne zachowanie, którym będziemy owijać inną funkcję, która go nie ma. Podając
    funkcję owijaną do dekoratora, jednocześnie pisząc w nim ów wrapper, udostępniamy tą funkcję wrapperowi,
    wykorzystując ją tak, jakby była zmienną lokalną dekoratora.

    wywołujemy funkcję dekorowaną we wrapperze, zapisując jej rezultat do zmiennej, którą zwracamy przy wywołaniu
    wrappera
    """
    def behavior_wrapping_function():
        """
        jak widać umieszczamy w funkcji inną funkcję, jest to tak zwana "zwijka" (wrapper), czyli owijamy funkcję w
        zachowanie które nam się podoba

        :return:
        """
        # here some behavior
        print(function.__name__)
        result = function()
        return result
    return behavior_wrapping_function


@print_name
def print_helloworld2():
    """
    następnie "DEKORUJEMY" funkcję, ubierając ją w zachowanie, robimy to za pomocą znaku "@" i następującej po niej
    nazwie dekoratora, w ten sposób określając zachowanie do udekorowania

    @nazwa_dekoratora umieszczamy ponad deklaracją funkcji dekorowanej
    """
    print('\n', 'in hello world')
    print('hello world')


def time_it(function):
    """
    Super, udekorowaliśmy naszą pierwszą funkcję,

    przejdźmy teraz do naszego przykładu z obliczaniem czasu wykonania funkcji i udekorujmy wszystkie poprzednie:

    *args i **kwargs są argumentami funkcji owijanej przez dekorator. Poprzednia funkcja, która była dekorowana nie
    przyjmował żadnych parametrów. Mogliśmy więc ten etap pominąć.

    Ale jak właściwie dzieje się to, że funkcja jest dekorowana?? Jak dziwaczna konstrukcja w postaci funkcji w funkcji
    może nam w jakikolwiek sposób pomóc przechwycić wartości funkcji, które podajemy na wejściu

    Odwołajmy się znowu do przypadku z funkcją jako zmienną. 2 przykłady wcześniej podaliśmy funkcję do innej funkcji
    jako zmienną. Następnie w funkcji ``print_function_name()`` wypisaliśmy jej nazwę, ale zwróciliśmy wynik jej
    działania. Zobaczmy jak wygląda tradycyjne wywołanie funkcji z zapisem do zmiennej:

    value = function_decorator(function_being_decorated)

    ale co jeżeli ta funkcja nie zwraca wartości, tylko inną funkcję?? w naszym przypadku wrapper? Czy to coś zmieni?

    Tak, będziemy mogli użyć WYWOŁANIA na zmiennej `value` dokładnie tak, jakby była funkcją

    new_value = value()

    i dopiero to zwróci nam wartość którą szukamy, jakoże `value` przechowywało definicję funkcji

    Ale to cały czas nie wyjaśnia działania dekoratora, możliwe że rzuca pewne światło, lecz nie wyjaśnia do końca

    To co robimy na prawdę wygląda bardziej tak (mimo, że zapis z nawiasami kwadratowymi nie jest poprawny):

    new_value = [value = function_decorator(function_being_decorated)]()

    co przechodzi w : new_value = function_decorator(function_being_decorated)()

    gdzie () na końcu natychmiastowo wywołuje funkcję która zwróciliśmy dekoratorem!!!

    A co jak mamy argumenty? poprzednio mieliśmy tylko czyste wywołanie funkcji które zwracało jakiś wynik.
    """
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print('\n', f"The function {function.__name__} took {end - start} to execute")
        return result
    return wrapper


@time_it
def fetch_data_decorated(server_adderss='www.server.com/api', data_type='int32'):
    """
    funkcja pobierająca dane z serwera, pobiera je i przetwarza do odpowiedniego formatu podanego w funkcji

    chwilę to trwa

    :param server_adderss: addres of a server which will be called to fetch data from
    :param data_type: type of data, default int32
    :return: data in desired format
    """
    print('fetching data...')
    sleep(0.5)
    print('preprocessing data...')
    sleep(0.5)
    print('done!')
    data = ['data']

    return data


@time_it
def add_decorated(a, b=1):
    return a + b


@time_it
def subs_decorated(a, b):
    return a - b


if __name__ == '__main__':
    '''
    mamy funkcje więc możemy zmierzyć czas ich wykonania. Jak to zrobić?
    
    z biblioteki time zaimportujemy sobie time, które zwraca czas systemowy od początku tzw. epoki, czyli od wybranego 
    momentu w historii ludzkości (1970 rok, 1 stycznia)
    '''

    print(datetime.now())
    epoch = time()
    print(datetime.fromtimestamp(epoch))
    print(datetime.fromtimestamp(0))

    custom_date = datetime(
        year=2019,
        month=1,
        day=20,
        hour=15,
        minute=24,
        second=57,
        microsecond=350
    )
    print(custom_date)

    '''
    to było kilka formalnych aspektów związanych z użytkowaniem modułu datetime orz time
    
    przejdźmy do mierzenia czasu wykonania naszej funkcji, możemy to zrobić na kilka sposobów, najprostszym z nich jest po 
    prostu zmierzenie czasu przed i po wykonaniu części kodu:
    '''

    start = time()
    data = fetch_data()
    end = time()
    time_taken = end - start
    print(time_taken)

    '''
    dostaniemy tutaj coś na styl 1 sekundy
    
    no dobrze, ale co jeżeli chcemy zmierzyć ten czas wiele razy? Co gdybyśmy mieli wiele metod/funkcji? 
    
    Można to zrobić tak:
    '''

    start = time()
    data1 = fetch_data()
    end = time()
    time_taken = end - start
    print(time_taken)

    start = time()
    data2 = fetch_data()
    end = time()
    time_taken = end - start
    print(time_taken)

    start = time()
    data3 = fetch_data()
    end = time()
    time_taken = end - start
    print(time_taken)

    start = time()
    result = add(20, 40)
    end = time()
    time_taken = end - start
    print(time_taken)

    start = time()
    result2 = add(10)
    end = time()
    time_taken = end - start
    print(time_taken)

    start = time()
    result3 = subs(41240, 1073.214)
    end = time()
    time_taken = end - start
    print(time_taken)

    '''
    trochę długi ten kod, nieładnie to wygląda. 
    
    natomiast po umieszczeniu pomiaru w funkcjach:
    '''

    add_timed(20)
    add_timed(30, 40)
    subs_timed(120, 124.2350)
    subs_timed(4001, 234.2309)
    fetch_data_timed()
    fetch_data_timed(server_adderss='www.goo.pl/api', data_type='float64')

    add_function = add
    print(add_function)  # <function object at ...>

    '''
    przekazanie funkcji do funkcji:
    '''

    print(print_function_name(print_helloworld))
    print_helloworld()

    '''
    funkcje dekorowane:
    '''

    print('\n', "after decorating:")
    print_helloworld2()

    print("after decorators")
    data1_deco = fetch_data_decorated()
    data2_deco = fetch_data_decorated()
    data3_deco = fetch_data_decorated()
    reult_deco = add_decorated(20)
    reult2_deco = add_decorated(30, 40)
    reult3_deco = subs_decorated(120, 124.2350)
    reult4_deco = subs_decorated(4001, 234.2309)
    reult5_deco = fetch_data_decorated()
    reult6_deco = fetch_data_decorated(server_adderss='www.goo.pl/api', data_type='float64')

    '''
    oraz to co pisaliśmy w time_it:
    '''
    result_deco_with_call = time_it(print_helloworld)()
    print(result_deco_with_call)
    result_deco_with_args = time_it(add)(1, 4)
    print(result_deco_with_args)

