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
    def __init__(self,nome,cpf,idade,email):
        self.validar_cpf(cpf)
        self.validar_email(email)
        self.nome = nome
        self.cpf = str(cpf)
        self.idade = idade
        self.email = email

    def validar_cpf(self, cpf):
        # self.cpf = str(self.cpf)
        padrao = re.compile("[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}")#padão do cpf   
        busca = padrao.match(cpf)
        if busca:
            if len(cpf) == 14 or len(cpf) == 11:#verificação do tamanho do cpf
                self.cpf = cpf
            else:
                raise ValueError('Tamanho de cpf invalido')
        else:
            raise ValueError('Formato de cpf invalido')

    def validar_email(self, email): 
        padrao = re.compile('[A-Za-z0-9_.-]+@[A-Za-z0-9_]+\.[a-z]{2,3}')
        busca = padrao.match(email)
        if busca :
            self.email = email
        else :
            raise ValueError('email invalido')

    def validar_idade (self):
        if self.idade <= 0 or self.idade >=130:
            raise ValueError('idade invalida')
        else:
            if self.idade <18 :
                raise ValueError('nao aceitamos menores de idade')
            else:
                print('idade valida')

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\nE-mail: {self.email}'

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
    
class ListaHostedes():
    pass

hospede = Hospede('joao','111.222.333-44', 18,'monteirowelley7@gmail.com')
print(hospede)
