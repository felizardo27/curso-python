
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes' 

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
        
    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
friends = Serie('friends', 1994, 10)
himym = Serie('How I met your mother', 2005, 9)
tmep = Filme('Todo mundo em pânico', 1999, 100)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
friends.dar_likes()
friends.dar_likes()
himym.dar_likes()
himym.dar_likes()
tmep.dar_likes()


filmes_e_series = [vingadores, friends, himym, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')



for programa in playlist_fim_de_semana:
    print(programa)

