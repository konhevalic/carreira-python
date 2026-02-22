from model.avaliacao import Avaliacao
class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return self._nome
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo} | {restaurante.media_avaliacoes}')

    @property
    def ativo(self):
        return 'algo' if self._ativo else  'false'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_avaliacoes = len(self._avaliacao)

        media = round(soma_notas / quantidade_avaliacoes, 1)

        return media
