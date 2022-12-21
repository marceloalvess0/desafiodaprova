#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Classes Hospede, Check-in e Check-out e Lista de Hospedes para elas faça:
# uma estrutura que cadastre o hospede
# uma estrutura que gere a lista de hospedes
# uma estrutura que registre o dia da entrada e o dia de saída
# mostre o valor que será pago pela estadia
# você deve validar o CPF, o e-mail do hospede
# o padrão de data 00/00/000 deve ser verificado tanto no check-in quanto no check-out
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos
import re
class Hospede :
    def __init__(self,nome,cpf,idade,email) :
        self.nome=nome
        self.cpf=cpf
        self.idade=idade
        self.email=email
    def valida_cpf(self):
        padrao = re.compile("([0-9]{3}.?){2}[0-9]{3}-?[0-9]{2}")    
        busca = padrao.match(self.cpf)
        if busca :
            print('ok')
class CheckIn():
    pass
class CheckOut():
    pass
class ListaHostedes(): 
    pass
h1=Hospede('sara','111.222.333-66',14,'sara@gmail.com')
h1.valida_cpf()