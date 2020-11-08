#
# Exemplo de como criar classes
#
class minhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou pelo construtor"

    def meuMetodo(self):
        print("Passou pelo meu metodo")

    def meuMetodo2(self, valor):
        self.outroValor = valor
        print(self.outroValor)

def criaObjetos():
    meuObj = minhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)
 
    meuObj.meuMetodo()

    meuObj.meuMetodo2("Executando meu metodo")

criaObjetos