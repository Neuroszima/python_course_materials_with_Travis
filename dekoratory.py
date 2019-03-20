"""
moduł - dekoratory

"""
from time import sleep, time
from datetime import datetime, date

'''
najprostszym i najbardziej popularnym przykładem do omawiania dekoratorów jest funkcjonalność mierzenia czasu wykonania
danej procedury czy też funkcji. Wyobraźmy sobie, że mamy już pewną procedurę, np. pobieramy dane z bazy i coś z nimi 
robimy. Funkcja taka zazwyczaj czeka na odbiór danych i sprawdza je, czy na pewno są odebrane we właściwej formie.

Załóżmy że coś w naszym programie nie gr i chcemy sprawdzić gdzie dokładnie, sprawdzając, jak długo dana 
funkcja/metoda/procedura się wykonuje
'''


def fetch_data(server_adderss='www.server.com/api', data_type='int32'):
    """
    funkcja pobierająca dane z serwera, pobiera je i przetwarza do odpowiedniego formatu podanego w funkcji

    chwilę to trwa

    :param server_adderss:addres of a server which will be called to fetch data from
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


'''
mamy funkcję więc możemy zmierzyć czas jej wykonania. Jak to zrobić?

z biblioteki time zaimportujemy sobie time, które zwraca czas systemowy od początku tzw. epoki, czyli od wybranego 
momentu w historii ludzkości
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

no dobrze, ale co jeżeli chcemy zmierzyć ten czas wiele razy? Można to zrobić tak:
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

'''
trochę długi ten kod, nieładnie to wygląda. Co gdybyśmy mieli wiele metod/funkcji?
'''


def add(a, b=1):
    return a + b


def subs(a, b):
    return a-b


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
musimy napisać/skopiować to zachowanie w wielu miejscach, a następnie nie zapomnieć usunąć tej części kodu ze wszystkich
części naszej biblioteki

czy jest prostsze rozwiązanie? Oczywiście. możemy np. zawrzeć to zachowanie w funkcji bezpośrednio.
'''


# noinspection PyPep8
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


def fetch_data_timed(server_adderss='www.server.com/api', data_type='int32'):
    """
    funkcja pobierająca dane z serwera, pobiera je i przetwarza do odpowiedniego formatu podanego w funkcji

    chwilę to trwa

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

# domyślnie kod gdzie indziej, we właściwym skrypcie


add_timed(20)
add_timed(30, 40)
subs_timed(120, 124.2350)
subs_timed(4001, 234.2309)
fetch_data_timed()
fetch_data_timed(server_adderss='www.goo.pl/api', data_type='float64')


'''
nieźle! nasz właściwy kod jest czystszy i bardziej czytelny, gdyż schowaliśmy pożądane zachowanie w naszych funkcjach

ale czy da się jeszcze lepiej? Co jeżeli mamy 100 różnych funkcji na przestrzeni całego programu?

Z pomocą przychodzą właśnie dekoratory

czym są dekoratory?

jest to dość specyficzne rozwiązanie pewnego nierzadko spotykanego problemu, ogólnie rzecz ujmując jest to sposób ubierania
funkcji w pewne zachowania, które chcemy zastosować w specyficznych miejscach

w naszym przykładzie chcemy ubrać nasze 3 funkcje w możliwość zmierzenia czasu ich wykonania, zróbmy to za pomocą 
dekoratora

W ramach wstępu musimy powiedzieć o jednej rzeczy, python jest żywym językiem, wszystko jest kodem który się wykonuje
nawet deklaracja definicji funkcji czy też utworzenia klasy

Dzięki temu wszystko co do tej pory widzieliśmy możemy potraktować jako zmienną, nie ważne czy jest to np. klasa czy 
funkcja. Możemy przypożądkować ją do zmiennej i na niej operować jakby była zwykłą zmienną
'''

add_function = add
print(add_function) # <function object at ...>

'''
co to oznacza? podstawową wiedzę już mamy, możemy przekazać zmienną do funkcji. A co jeśli tą zmienną bęzie inna 
funkcja? Jest to podstawą dekorowania funkcji w inne zachowania

Rozpatrzmy prosty przypadek
'''


def print_helloworld():
    print('\n', 'in hello world')
    print('hello world')


def print_function_name(function):
    print('in "print function name"')
    result = function()
    print(function.__name__)
    return result


print(print_function_name(print_helloworld))
print_helloworld()

'''
w ten sposób udekorowaliśmy funkcję w zachowanie innej funkcji; wypisaliśmy nazwę funkcji a następnie wewnątrz funkcji 
dekorującej, wykonaliśmy funkcję dekorowaną, zwracając na końcu jej rezultat

a jak zrobilibyśmy to bardziej ogólnie? W następujący sposób
'''


def print_name(function):
    def behavior_wrapping_function():
        # here some behavior
        print(function.__name__)
        result = function()
        return result
    return behavior_wrapping_function


'''
następnie "DEKORUJEMY" funkcję, ubierając ją w zachowanie, robimy to za pomocą znaku "@" i następującej po niej nazwie
dekoratora, w ten sposób określając zachowanie do udekorowania
'''


@print_name
def print_helloworld2():
    print('\n', 'in hello world')
    print('hello world')


print('\n', "after decorating:")
print_helloworld2()


'''
Super, udekorowaliśmy naszą pierwszą funkcję, 

przejdźmy teraz do naszego przykładuz obliczaniem czasu wykonania funkcji i udekorujmy wszystkie poprzednie:
'''


def time_it(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print('\n', f"The function {function.__name__} took {end - start} to execute")
        return result
    return wrapper


@time_it
def fetch_data(server_adderss='www.server.com/api', data_type='int32'):
    """
    funkcja pobierająca dane z serwera, pobiera je i przetwarza do odpowiedniego formatu podanego w funkcji

    chwilę to trwa

    :param server_adderss:addres of a server which will be called to fetch data from
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
def add(a, b=1):
    return a + b


@time_it
def subs(a, b):
    return a-b


print("after decorators")
data1_deco = fetch_data()
data2_deco = fetch_data()
data3_deco = fetch_data()
reult_deco = add(20)
reult2_deco = add(30, 40)
reult3_deco = subs(120, 124.2350)
reult4_deco = subs(4001, 234.2309)
reult5_deco = fetch_data()
reult6_deco = fetch_data(server_adderss='www.goo.pl/api', data_type='float64')
