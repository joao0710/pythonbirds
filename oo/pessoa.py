class Pessoa:
    def __init__(self, *filhos, nome, idade=25):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    for filhos in luciano.filhos:
        print(f'São filhos de {luciano.nome}: {filhos.nome}')
