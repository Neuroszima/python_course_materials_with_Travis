"""
dwie funkcje hello world

pozornie robią to samo ale na inny sposób
"""
# if __name__ == '__main__':


def hello_world_function():
    return "hello world from function"


def hello_world_function2():
    print("hello world from function")


"""
funkcje mogą też przerabiać pewne dane i zwracać wyniki działania

np. poniższe funkcje
"""


def suma(a, b):
    """
    funkcja przyjmuje dwie wartości i zwrca ich sumę

    :param a: 1 wartość
    :param b: 2 wartość
    :return: a + b
    """

    return a + b


"""
Ćwiczenie 1. zadeklaruj funkję która mnoży
"""


"""
a co się stanie jeżeli robimy taką funkcję?

"""


def sum(a, b):
    """
    robi to samo co wyżej, ale nadpisywana jest wbudowana metoda sum(a, b)
    :param a:
    :param b:
    :return:
    """
    return a + b


def foo(a, b):
    """
    funkcje możemy wywoływać w innych funkcjach
    :param a:
    :param b:
    :return:
    """
    result = sum(a, b)
    return result


def foo2(a, b=3):
    """
    ta funkja przyjmuje 2 wartości, ale może też przyjąc 1
    wartość b przyjmie wartość domyślną 3
    :param a:
    :param b: możliwa do nadpisania wartość
    :return:
    """
    return a + b


"""
Ćwiczenie 2. zadeklaruj funkję gęstość
"""

"""
jeżeli chcialibyśmy azadeklarować funkcję która nie wiadomo ile argumentów będzie przyjmować?
"""


def function(A, radius, *args, file="test.txt", other_arguments=["something", "type"]):
    """
    przyjmuje powierzchnię oraz promień danej kuli i zapisuje je do pliku

    dobyślny zapis do pliku `test.txt`, pozostałe argumenty umożliwiają pożądane formatowanie tekstu


    :param A:
    :param radius:
    :param file:
    :param args:
    :return:
    """
    print(args)
    print(A)
    print(radius)
    print(file)
    for arg in other_arguments:
        print(arg)


def function_kwargs(A, radius, file="test.txt", **kwargs):
    """
    przyjmuje powierzchnię oraz promień danej kuli i zapisuje je do pliku

    dobyślny zapis do pliku `test.txt`, pozostałe argumenty umożliwiają pożądane formatowanie tekstu


    :param A:
    :param radius:
    :param file:
    :param args:
    :return:
    """

    print(A)
    print(radius)
    print(file)
    for key in kwargs:
        print(key, " ", kwargs[key])
    return (A, radius, file, kwargs)


if __name__ == '__main__':
    print(foo(2, 3)) # 5
    print(foo2(2, 5))  # 7
    print(foo2(4))  # 7
    function(20, 40, file="something.txt")
    function_kwargs(20, 40, file="something.txt", type="text", object_type="sphere")
