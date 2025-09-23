'''
Crear una lista de las permutaciones de una lista de números (utilizando `itertools.permutations()`).
Por ejemplo, si introducimos la lista (1,2,3) deberíamos obtener un resultado similar a
`[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]`.
Crea también una lista de las permutaciones de una palabra.
'''
import itertools
quePermutar=input("Que quieres permutar? ").strip()
permutaciones=[permutacion for permutacion in itertools.permutations(quePermutar)]
print(permutaciones)