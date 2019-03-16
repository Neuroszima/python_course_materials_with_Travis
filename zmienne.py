"""
pierwsze kroki w zmiennych

"""


'''
    a co jeżeli chcielibyśmy wpisać wartość tylko taką jaką chcemy, a jeszcze jej nie znamy 
    przed uruchomieniem programu?

    tutaj jest przydatna funkcja "input"
'''

# a = input('podaj a: ')
# b = input('podaj b: ')

# print(a + b)

'''
dlaczego dodało 3 + 7 i wyszło 37?

nasz skrypt dodał te dwie zmienne tak jakby były one tekstem

trzeba skonwertować dane z klawiatury na typ liczbowy, np. "int"
'''

# a = int(input('podaj a: '))
# b = int(input('podaj b: '))

# print(a + b)

'''
możemy definiować różne typy zmiennych, np. 
    łańcuch znaków              (string)
    liczbę całkowitą            (integer)
    wartość prawda/fałsz        (boolean)
    liczbę zmiennoprzecinkową   (float)
'''

i = 4
s = "5"
b = True
f = .0

'''
możemy sprawdzać typ zmiennej stosując funkcję "type" albo "isinstance"

w ten sposób możemy sprawdzić czy zmienne odpowiadają temu typowi który chcemy:
'''

print(isinstance(i, int))
print(type(b))
print(isinstance(b, bool))
print(type(f))

if isinstance(b, bool):
    print("działam poprawnie")
else:
    print("podałeś złe dane, spróbuj jeszcze raz")

print(type(f) == float)
print(type(f))
print(type(float))
print(float)

if type(f) == float:
    c = 15. + f
    print(c)
else:
    print("incorrect data type")

'''
co się stanie gdy to do siebie dodamy? czy kolejność ma znaczenie?
'''

# print(a + b)
# print(b + a)

'''
nie możemy dodać do siebie tych zmiennych od razu, musimy je przekonwertować na typ który umożliwia nam ich dodawanie
czyli na wspólny

'''

'''
dobra a co jeżeli byśmy chcieli pomnóżyć przez coś tekst?
'''

print("AAAAAAAAAA" * 10)

