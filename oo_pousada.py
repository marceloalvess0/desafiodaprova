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
from datetime import datetime
class Hospede :
    def __init__(self,nome,cpf,idade,email) :
        self.nome=nome ##encapsular
        self.cpf=cpf ##encapsular
        self.idade=idade ##encapsular
        self.email=email ##encapsular
        
    def valida_cpf(self):
        self.cpf = str(self.cpf)
        padrao = re.compile("([0-9]{3}.?){2}[0-9]{3}-?[0-9]{2}")    
        busca = padrao.match(self.cpf)
        if busca :
            print('cpf valido')
        else:
            raise ValueError('cpf invalido')
    def valida_email(self): 
        padrao = re.compile('[A-Za-z0-9_.-]+@[A-Za-z0-9_]+\.[a-z]{2,3}')
        busca = padrao.match(self.email)
        if busca :
            print('email valido')
        else :
            raise ValueError('email invalido')
    def valida_idade (self):
        if self.idade <= 0 or self.idade >=130:
            raise ValueError('idade invalida')
        else:
            if self.idade <18 :
                raise ValueError('nao aceitamos menores de idade')
            else:
                print('idade valida')
class CheckIn():
    def __init__(self,data_entrada):
        self.data_entrada = data_entrada
        
    def valida_data(self):
        padrao = re.compile("[1-3][0-9]/[0-1][0-9]/[1-9][0-9]{3}")
        match = padrao.match()
        if match:
            print("Data válida")
        else:
            raise ValueError ("Data inválida")
    def formata_data(self):
        self.data_entrada = datetime.strptime(self.data_entrada, "%d/%m/%Y")
        print(self.data_entrada)
        return self.data_entrada
    
class CheckOut():
    def __init__(self,data_saida):
        self.data_saida = data_saida
        
    def valida_data(self):
        padrao = re.compile("[1-3][0-9]/[0-1][0-9]/[1-9][0-9]{3}")
        match = padrao.match()
        if match:
            print("Data válida")
        else:
            raise ValueError ("Data inválida")
    def formata_data(self):
        self.data_saida = datetime.strptime(self.data_saida, "%d/%m/%Y")
        print(self.data_saida)
        return self.data_saida
    
class ListaHospedes():
    pass


hospede = CheckIn("10/09/2000")
dia_entrada = hospede.formata_data()
hospede1 = CheckOut("13/09/2000")
dia_saida =hospede1.formata_data()
quantidade_dias = abs(dia_saida - dia_entrada)
print(hospede)
print(quantidade_dias)