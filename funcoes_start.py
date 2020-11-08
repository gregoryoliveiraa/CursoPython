#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def func1():
    print("Eu sou uma funcao")

func1()
# função que recebe argumentos
def func2(arg1, arg2):
    print(arg1 + " " + arg2)

func2("Gregory", "Oliveira")

# função que retorna um valor

def cubo(x):
    return x * x * x

f = cubo(3)
print(f)