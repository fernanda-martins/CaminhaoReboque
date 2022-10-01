class Veiculo:
    def __init__(self,mod,pot,*comb):
        self.modelo      = mod
        self.potencia    = pot
        self.combustivel = [] #lista
        for x in comb: #para add intens na LISTA precisa de FOR e APPEND(add 1 por vez)
            self.combustivel.append(x)

    def add_combustivel(self,combustivel): #funçao p add mais opcoes de comb depois
        self.combustivel.append(combustivel)

    def lista_combustiveis(self):
        return self.combustivel

class Automovel(Veiculo):
    def __init__(self,mod,pot,comb,num):
        super().__init__(mod,pot,comb)
        self.numero = num

    def consumo(self):
        consumo = self.potencia / 10
        if 'alcool' in self.combustivel: #item na lista
            consumo = consumo * 1.3
        return consumo
    pass

class CaminhaoReboque(Veiculo):
    def __init__(self,mod,pot,comb,cap): #aqui coloca todas as variaveis que o usuário vai declarar, reb nao precisa pq é none
        super().__init__(mod,pot,comb)
        self.capacidade_carga = cap
        self.__rebocando  = None

    def rebocar(self,auto):
        self.__rebocando = auto #rebocando recebe o auto que está rebocando

    def liberar(self):
        self.__rebocando = None #rebocando recebe none

    def mostraReboque(self):
        return self.__rebocando

#CRIAÇÃO DE OBJETOS

c1 = Automovel('Fiat',100,'alcool',4)
c1.add_combustivel('gasolina')
print(f'O automovel {c1.modelo} usa {c1.combustivel} como combustível')
print(f'Consumo desse automóvel é de {c1.consumo()} km/l')

r1 = CaminhaoReboque('Ford',800,'alcool',2)
r1.add_combustivel('diesel')
r1.rebocar(c1)
print(f'O automovel {r1.mostraReboque().modelo} está sendo rebocado')
r1.liberar() #nao tem o atributo auto
if r1.mostraReboque() == None:
    print('Nunhum veiculo esta sendo rebocado')
