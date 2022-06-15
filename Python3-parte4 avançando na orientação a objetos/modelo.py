
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes {vingadores.likes}')


friends = Serie('friends', 1994, 10)
friends.dar_like()
friends.nome = 'amigos'
print(f'Nome: {friends.nome} - Ano: {friends.ano} - Temporadas: {friends.temporadas} - Likes {friends.likes}')
