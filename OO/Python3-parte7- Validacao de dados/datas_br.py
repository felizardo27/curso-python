from datetime import datetime, timedelta

'''
Caracteres	Descrição	                Exemplos
%A	        Dias da semana por extenso	Sunday, Monday, ...
%d	        Dias do mês	                01, 02, ..., 31
%m	        Meses em formato de números	01, 02, ..., 12
%y	        Ano em formato de 2 dígitos	99, 15
%Y	        Ano em formato de 4 dígitos	1993, 2011
%H	        Hora em formato decimal	    00, 01, ..., 23
%M	        Minuto em formato decimal	00, 01, ..., 59
%S	        Segundo em formato decimal	00, 01, ..., 59
'''

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()   
     
    def __str__(self):
        return self.format_data()
     
    def mes_cadastro(self):
        mes = self.momento_cadastro.month
        meses = ("Janeiro", "Fevereiro", "Março", "Abirl", "Maio", "Junho", 
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        return meses[mes-1]
    
    def semana_cadastro(self):
        semana = self.momento_cadastro.weekday()
        semana_lista = ("Segunda-feira", "Terça-feira",
                   "Quarta-feira", "Quinta-feira",
                   "Sexta--feira", "Sabado", "Domingo")
        return semana_lista[semana]
    
    def format_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y - %H:%M")
    
    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=15, minutes=20,seconds=30)) - self.momento_cadastro