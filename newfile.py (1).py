print('hecho by ixo')
name = input('cual es tu nombre?\n')
print('hola, %s!' % name)

import random

maxn = 10
n = random.randint(1, maxn)
print('adivina el num')
print('esta entre 1 y %d' % maxn)
guess = None
while guess != n:
    guess = int(input('tu intento '))
    if guess > n:
        print('alto')
    if guess < n:
        print('bajo')

print('ganaste!')