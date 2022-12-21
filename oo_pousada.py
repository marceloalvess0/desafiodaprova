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
import datetime
class Hospede :
    def __init__(self,nome,cpf,idade,email) :
        self.nome=nome
        self.cpf=self.valida_cpf(cpf)
        self.idade=self.valida_idade(idade)
        self.email=self.valida_email(email)
    def valida_cpf(self,cpf):
        self.cpf = str(cpf)
        padrao = re.compile("([0-9]{3}.?){2}[0-9]{3}-?[0-9]{2}")    
        busca = padrao.match(cpf)
        if busca :
            print('cpf valido')
            self.cpf = cpf
        else:
            raise ValueError('cpf invalido')
    def valida_email(self,email): 
        padrao = re.compile('[A-Za-z0-9_.-]+@[A-Za-z0-9_]+\.[a-z]{2,3}')
        busca = padrao.match(email)
        if busca :
            print('email valido')
            self.email=email
        else :
            raise ValueError('email invalido')
    def valida_idade (self,idade):
        if idade <= 0 or idade >=130:
            raise ValueError('idade invalida')
        else:
            if idade <18 :
                raise ValueError('nao aceitamos menores de idade')
            else:
                print('idade valida')
                self.idade = idade
class CheckIn():
    def __init__(self,data_entrada):
        self.data_entrada = data_entrada
        
    def valida_data(self):
        padrao = re.compile("[1-3][0-9]/[0-1][0-9]/[1-9][0-9]{3}")
        match = padrao.match(self.data_entrada)
        if match:
            print("Data válida de entrada")
            dia = int(self.data_entrada[0:2])
            mes = int(self.data_entrada[3:5])
            ano = int(self.data_entrada[6::])
            entrada=datetime.date(ano,mes,dia)
            self.e=entrada.day
            print(entrada)
        else:
            raise ValueError ("Data inválida")
class CheckOut(CheckIn):
    def __init__(self, data_entrada,data_saida):
        super().__init__(data_entrada)
        self.data_saida=data_saida
    def valida_data(self):
        padrao = re.compile("[1-3][0-9]/[0-1][0-9]/[1-9][0-9]{3}")
        match = padrao.match(self.data_saida)
        if match :
            print("Data válida de saida")
            dia = int(self.data_saida[0:2])
            mes = int(self.data_saida[3:5])
            ano = int(self.data_saida[6::])
            saida=datetime.date(ano,mes,dia)
            self.s=saida.day
            print(saida)
        else:
            raise ValueError ("Data inválida")
    def quant_dias (self,data_entrada,data_saida):
        if self.valida_data :
            dia = int(data_entrada[0:2])
            mes = int(data_entrada[3:5])
            ano = int(data_entrada[6::])
            self.entrada=datetime.date(ano,mes,dia)
            dia2 = int(data_saida[0:2])
            mes2 = int(data_saida[3:5])
            ano2 = int(data_saida[6::])
            self.saida=datetime.date(ano2,mes2,dia2)
            self.conta= self.saida-self.entrada
            print(f'voce ficou {self.conta.days} dias')
    def conta_pagar(self,dinhero):
        print('a estadia é 50 reais por dia')
        conta = 50 * self.conta.days
        if dinhero <=0 or dinhero < conta:
            raise ValueError('dinhero invalido')
        elif dinhero == conta : 
            print(f'sua conta de {conta} foi paga')
        if self.entrada == self.saida :
            conta = 40.0 * 1
            if dinhero == conta : 
                print(f'sua conta de {conta} foi paga')
            elif dinhero > conta :
                troco=dinhero - conta
                print(f'seu troco foi {troco} e sua conta foi {conta}')
        else :
            troco=dinhero - conta
            print(f'seu troco foi {troco} e sua conta foi {conta}')
class ListaHospedes():
    def __init__(self,nome,hospede):
        self.nome=nome
        self.hospede=hospede
    def __getitem__ (self,item) :
        return self.hospede[item]
    @property
    def listagem (self) :
        return self.hospede
    @property
    def __len__ (self) :
        return len(self.hospede)
sara = Hospede('sara','11122233344',18,'sara@gmail.com')
sara = CheckIn('10/03/2022')
sara.valida_data()
sara = CheckOut('10/03/2022','10/04/2022')
sara.valida_data()
sara.quant_dias('10/03/2022','10/04/2022')
sara.conta_pagar(1550)
ray = Hospede('ray','11122233334',20,'ray@gmail.com')
ray = CheckIn('17/03/2022')
ray.valida_data()
ray = CheckOut('17/03/2022','18/04/2022')
ray.valida_data()
ray.quant_dias('17/03/2022','18/04/2022')
ray.conta_pagar(2000)
lista_hospedes=['sara','11122233344',18,'sara@gmail.com'],['ray','11122233334',20,'ray@gmail.com']
lista_visitas=ListaHospedes('visitas',lista_hospedes)
c=1
for v in lista_visitas.listagem:
    print(f'hospede {c} tem os agurmentos {v}')
    c+=1